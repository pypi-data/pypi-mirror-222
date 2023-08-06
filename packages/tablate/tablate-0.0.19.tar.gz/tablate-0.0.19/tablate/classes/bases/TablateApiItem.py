from typing import Union, Callable

from tablate.classes.bases.TablateApiBase import TablateApiBase


class TablateApiItem(TablateApiBase):

    def to_dict(self):
        pass

    def apply(self, function: Callable[[dict, dict], (dict, dict)]):
        frame_dict, globals_dict = function(self._frame_list[0], self._globals)
        if frame_dict is not None:
            self._frame_list[0] = frame_dict
        if globals_dict is not None:
            self._globals = globals_dict