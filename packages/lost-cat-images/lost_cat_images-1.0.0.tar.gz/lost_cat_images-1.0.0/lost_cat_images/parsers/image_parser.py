""""""
import os
import logging
import PIL.Image, PIL.ExifTags
from lost_cat.parsers.base_parser import BaseParser

from lost_cat.utils.tag_anon import TagAnon

logger = logging.getLogger(__name__)

class EXIFParser(BaseParser):
    """

    ---
    Attributes
    ----------
    Methods
    -------

    """

    def __init__(self, uri: str = None, bytes_io: bytes = None, settings: dict = None) -> None:
        super().__init__(uri=uri, bytes_io=bytes_io, settings=settings)
        self._version = "0.0.1"
        self._name = f"{self.__class__.__name__.lower()} {self._version}"

        if not settings:
            logger.debug("Loading default settings")
            #self.settings = DICOMParser.avail_config()

        logger.debug("Name: %s", self._name)
        logger.debug("Settings: %s", self.settings)

        # file
        self._uri = None
        self._file = None
        if uri:
            self._uri = uri
            self._file = PIL.Image.open(uri)

        elif bytes_io:
            #self._file = <TODO: add byte stream handler>
            pass

    def __str__(self):
        return f"{self.name} {self.version} <{self._uri}>"

    def close(self) -> None:
        """"""
        if self._file:
            self._file = None

    def get_extensions(self):
        """

        Parameters
        ----------
        Returns
        -------
        None
        """
        return [".bmp",".dds",".dib",".eps",".gif",".icns",".ico",".im",".jpeg",".msp",".pcx",".png",".ppm",
        ".sgi",".tga",".tiff",".webp",".xbm",".blp",".cur",".dcx",".fli",".flc",".fpx",".ftex",".gbr",".gd",
        ".imt",",iptc",".naa",".mcidas",".mic",".mpo",".pcd",".pixar",".psd",".wal",".wmf",",xpm"]

    def get_functions(self):
        """

        Parameters
        ----------
        Returns
        -------
        None
        """
        return {
            "metadata": self.get_metadata,
            "analyze": self.analyze,
            #"contents": self.get_contents
        }

    def get_metadata(self) -> dict:
        """This will return the doc info infomation from the
        Named file.

        Parameters
        ----------
        Returns
        -------
        None
        """
        width, height = self._img.size
        tags = {PIL.ExifTags.TAGS[k]: v for k, v in self._img._getexif().items() if k in PIL.ExifTags.TAGS}
        data = {
            "width": width,
            "height": height,
            "tags": tags,
            "mode": self._img.mode,
            "info": self._img.info,
            "bands": list(self._img.getbands())
        }
        return data

    def analyze(self) -> dict:
        """

        Parameters
        ----------
        Returns
        -------
        None
        """
        data = dict

        return data

    def get_contents(self) -> list:
        """This will return the paragroah objects in a word document

        Parameters
        ----------
        Returns
        -------
        None
        """
        data = []

        return data