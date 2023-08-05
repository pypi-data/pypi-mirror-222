from __future__ import annotations

import io
import struct
from pathlib import Path

import numpy as np
from construct import ListContainer
from PIL import Image

from oct_converter.image_types import FundusImageWithMetaData, OCTVolumeWithMetaData
from oct_converter.readers.binary_structs import fda_binary


class FDA(object):
    """Class for extracting data from Topcon's .fda file format.

    Attributes:
        filepath: path to .fda file for reading.
        chunk_dict: names of data chunks present in the file, and their start locations.
    """

    def __init__(self, filepath: str | Path, printing: bool = True) -> None:
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(self.filepath)

        self.chunk_dict = self.get_list_of_file_chunks(printing=printing)

    def get_list_of_file_chunks(self, printing: bool = True) -> dict:
        """Find all data chunks present in the file.

        Returns:
            dictionary of chunk names, containing their locations in the file and size.
        """
        chunk_dict = {}
        with open(self.filepath, "rb") as f:
            # skip header
            raw = f.read(15)
            header = fda_binary.header.parse(raw)

            eof = False
            while not eof:
                chunk_name_size = np.fromstring(f.read(1), dtype=np.uint8)[0]
                if chunk_name_size == 0:
                    eof = True
                else:
                    chunk_name = f.read(chunk_name_size)
                    chunk_size = np.fromstring(f.read(4), dtype=np.uint32)[0]
                    chunk_location = f.tell()
                    f.seek(chunk_size, 1)
                    if chunk_name in chunk_dict.keys():
                        previous_location = chunk_dict[chunk_name][0]
                        previous_size = chunk_dict[chunk_name][1]
                        if not isinstance(previous_location, list):
                            previous_location = [previous_location]
                            previous_size = [previous_size]
                        chunk_location = previous_location + [chunk_location]
                        chunk_size = previous_size + [chunk_size]

                    chunk_dict[chunk_name] = [chunk_location, chunk_size]
        if printing:
            print("File {} contains the following chunks:".format(self.filepath))
            for key in chunk_dict.keys():
                print(key)
            print("")
        return chunk_dict

    def read_oct_volume(self) -> OCTVolumeWithMetaData:
        """Reads OCT data.

        Notes:
            Mostly based on description of .fda file format here:
            https://bitbucket.org/uocte/uocte/wiki/Topcon%20File%20Format

        Returns:
            OCTVolumeWithMetaData
        """

        if b"@IMG_JPEG" not in self.chunk_dict:
            print("@IMG_JPEG is not in chunk list, skipping.")
            return None
        with open(self.filepath, "rb") as f:
            chunk_location, chunk_size = self.chunk_dict[b"@IMG_JPEG"]
            f.seek(chunk_location)  # Set the chunk’s current position.
            raw = f.read(25)
            oct_header = fda_binary.oct_header.parse(raw)

            volume = []
            for i in range(oct_header.number_slices):
                size = np.fromstring(f.read(4), dtype=np.int32)[0]
                raw_slice = f.read(size)
                image = Image.open(io.BytesIO(raw_slice))
                volume.append(np.asarray(image))

        # read segmentation contours if possible and store them as distance
        # from top of scan to be compatible with plotting in OCTVolume
        contours = self.read_segmentation()
        if contours:
            contours = {k: oct_header.height - v for k, v in contours.items()}

        # read all other metadata
        metadata = self.read_all_metadata()

        oct_volume = OCTVolumeWithMetaData(volume, contours=contours, metadata=metadata)
        return oct_volume

    def read_oct_volume_2(self) -> OCTVolumeWithMetaData:
        """Reads OCT data. Worth trying if read_oct_volume fails.

        Returns:
            OCTVolumeWithMetaData
        """

        if b"@IMG_MOT_COMP_03" not in self.chunk_dict:
            print("@IMG_MOT_COMP_03 is not in chunk list, skipping.")
            return None
        with open(self.filepath, "rb") as f:
            chunk_location, chunk_size = self.chunk_dict[b"@IMG_MOT_COMP_03"]
            f.seek(chunk_location)  # Set the chunk’s current position.
            raw = f.read(22)
            oct_header = fda_binary.oct_header_2.parse(raw)
            number_pixels = (
                oct_header.width * oct_header.height * oct_header.number_slices
            )
            raw_volume = np.fromstring(f.read(number_pixels * 2), dtype=np.uint16)
            volume = np.array(raw_volume)
            volume = volume.reshape(
                oct_header.width, oct_header.height, oct_header.number_slices, order="F"
            )
            volume = np.transpose(volume, [1, 0, 2])
        oct_volume = OCTVolumeWithMetaData(
            [volume[:, :, i] for i in range(volume.shape[2])]
        )
        return oct_volume

    def read_fundus_image(self) -> FundusImageWithMetaData:
        """Reads fundus image.

        Returns:
            FundusImageWithMetaData
        """
        if b"@IMG_FUNDUS" not in self.chunk_dict:
            print("@IMG_FUNDUS is not in chunk list, skipping.")
            return None
        with open(self.filepath, "rb") as f:
            chunk_location, chunk_size = self.chunk_dict[b"@IMG_FUNDUS"]
            f.seek(chunk_location)  # Set the chunk’s current position.
            raw = f.read(24)  # skip 24 is important
            fundus_header = fda_binary.fundus_header.parse(raw)
            number_pixels = fundus_header.width * fundus_header.height * 3
            raw_image = f.read(fundus_header.size)
            image = Image.open(io.BytesIO(raw_image))
            image = np.asarray(image)
            # store with RGB channel order
            image = np.flip(image, 2)
        fundus_image = FundusImageWithMetaData(image)
        return fundus_image

    def read_fundus_image_gray_scale(self) -> FundusImageWithMetaData:
        """Reads grayscale fundus image.

        Returns:
            FundusImageWithMetaData
        """
        if b"@IMG_TRC_02" not in self.chunk_dict:
            print("@IMG_TRC_02 is not in chunk list, skipping.")
            return None
        with open(self.filepath, "rb") as f:
            chunk_location, chunk_size = self.chunk_dict[b"@IMG_TRC_02"]
            f.seek(chunk_location)  # Set the chunk’s current position.
            raw = f.read(21)  # skip 21 is important
            img_trc_02_header = fda_binary.img_trc_02_header.parse(raw)
            number_pixels = img_trc_02_header.width * img_trc_02_header.height * 1
            raw_image = f.read(img_trc_02_header.size)
            image = Image.open(io.BytesIO(raw_image))
            image = np.asarray(image)
        fundus_gray_scale_image = FundusImageWithMetaData(image)
        return fundus_gray_scale_image

    def read_segmentation(self) -> dict:
        """Reads layer segmentation data.

        Segmentation values are returned in a dictionary with a key for every
        layer boundary and are measured in pixels from B-scan bottom.

        Returns
            dictionary with segmentation data.
        """

        if b"@CONTOUR_INFO" not in self.chunk_dict.keys():
            print("The file does not have any segmentation chunk.")
            return None

        layer = {
            "MULTILAYERS_1": "ILM",
            "MULTILAYERS_2": "RNFL_GCL",
            "MULTILAYERS_3": "GCL_IPL",
            "MULTILAYERS_4": "IPL_INL",
            "MULTILAYERS_5": "MZ_EZ",
            "MULTILAYERS_6": "IZ_RPE",
            "MULTILAYERS_7": "BM",
            "MULTILAYERS_8": "INL_OPL",
            "MULTILAYERS_9": "ELM",
            "MULTILAYERS_10": "CSI",
        }

        seg_dict = {}
        with open(self.filepath, "rb") as f:
            for pos in self.chunk_dict[b"@CONTOUR_INFO"][0]:
                f.seek(pos)
                raw = f.read(34)
                header = dict(fda_binary.__dict__["contour_info_header"].parse(raw))
                n_voxel = header["width"] * header["height"]

                data_bytes = f.read(n_voxel * 2)
                seg = struct.unpack("H" * n_voxel, data_bytes)
                seg = np.array(seg).reshape((header["height"], header["width"]))
                seg = np.flip(seg, 0)
                layer_name = layer.get(header["id"], header["id"])
                seg_dict[layer_name] = seg

        return seg_dict

    def read_all_metadata(self, verbose: bool = False):
        """
        Reads all available metadata and returns a dictionary.

        Args:
            verbose: if True, prints the chunks that are not supported.

        Returns:
            dictionary with all metadata.
        """
        metadata = dict()
        for key in self.chunk_dict.keys():
            if key in [b"@IMG_JPEG", b"@IMG_FUNDUS", b"@IMG_TRC_02", b"@CONTOUR_INFO"]:
                # these chunks have their own dedicated methods for extraction
                continue
            json_key = key.decode().split("@")[-1].lower()
            try:
                metadata[json_key] = self.read_any_info_and_make_dict(key)
            except KeyError:
                if verbose:
                    print(f"{key} there is no method for getting info from this chunk.")
        return metadata

    def read_any_info_and_make_dict(self, chunk_name: str) -> dict:
        """Reads any chunk and constructs a dictionary.

        Args:
            chunk_name: name of the chunk which data will be taken.

        Returns:
            Chunk info data
        """
        if chunk_name not in self.chunk_dict:
            print(f"{chunk_name} is not in chunk list, skipping.")
            return None
        with open(self.filepath, "rb") as f:
            chunk_location, chunk_size = self.chunk_dict[chunk_name]
            f.seek(chunk_location)  # Set the chunk’s current position.
            raw = f.read()
            header_name = f"{chunk_name.decode().split('@')[-1].lower()}_header"
            chunk_info_header = dict(fda_binary.__dict__[header_name].parse(raw))
            chunks_info = dict()
            for idx, key in enumerate(chunk_info_header.keys()):
                if idx == 0:
                    continue
                if type(chunk_info_header[key]) is ListContainer:
                    chunks_info[key] = list(chunk_info_header[key])
                else:
                    chunks_info[key] = chunk_info_header[key]
        return chunks_info
