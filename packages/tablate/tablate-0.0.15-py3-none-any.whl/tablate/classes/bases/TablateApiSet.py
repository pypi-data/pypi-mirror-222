from typing import Union

from tablate.classes.bases.TablateApiBase import TablateApi
from tablate.classes.helpers.get_frame import get_frame
from tablate.classes.helpers.list_frame import list_frames


class TablateSet(TablateApi):

    def list_frames(self):
        list_frames(self._frame_list)

    def get_frame(self, selector: Union[int, str]):
       return get_frame(frame_list=self._frame_list, options=self._options, selector=selector)

    def from_dict(self):
        pass

    def remove_frame(self):
        pass

    def replace_frame(self):
        pass