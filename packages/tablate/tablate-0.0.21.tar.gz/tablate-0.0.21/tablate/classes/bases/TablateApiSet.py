from typing import Union, Callable, Tuple

from tablate.classes.bases.TablateApiBase import TablateApiBase
from tablate.classes.helpers.get_frame import get_frame
from tablate.classes.helpers.list_frame import list_frames


class TablateApiSet(TablateApiBase):

    def apply(self, function: Callable[[dict, dict],Tuple[dict, dict]]):
        frame_list, globals_dict = function(self._frame_list, self._globals)
        if frame_list is not None:
            self._frame_list = frame_list
        if globals_dict is not None:
            self._globals = globals_dict

    def list_frames(self):
        list_frames(self._frame_list)

    def get_frame(self, selector: Union[int, str], apply_globals: bool = False):
        if apply_globals:
            return get_frame(frame_list=self._frame_list, selector=selector, globals=self._globals)
        else:
            return get_frame(frame_list=self._frame_list, selector=selector)

    def from_dict(self):
        pass

    def remove_frame(self, selector: Union[int, str]):
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if (type(selector) == int and selector == frame_index) or (type(selector) == str and selector == frame_key):
                del self._frame_list[frame_key]
                break

    def replace_frame(self, selector: Union[int, str], new_frame):
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if (type(selector) == int and selector == frame_index) or (type(selector) == str and selector == frame_key):
                for new_frame_key, new_frame_item in new_frame._frame_list.items():
                    self._frame_list[frame_key] = new_frame_item
                    break