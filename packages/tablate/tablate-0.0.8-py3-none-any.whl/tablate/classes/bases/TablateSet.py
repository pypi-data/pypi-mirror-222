from copy import deepcopy

from tablate.classes.bases.TablateApi import TablateApi
from tablate.type.primitives import FrameDivider, OuterBorder


class TablateSet(TablateApi):

    def __init__(self,
                 tablate_set: list,  # this is a list of TablateUnion... circular imports prevents self from being included
                 outer_border: OuterBorder = "thick",
                 outer_padding: int = 1,
                 frame_divider: FrameDivider = "thick",
                 outer_width: int = None,
                 html_px_size: int = 6,
                 html_text_size: int = 12,
                 html_outer_width: str = "100%",
                 html_css_injection: str = ""):

        super().__init__(outer_border=outer_border,
                         outer_padding=outer_padding,
                         frame_divider=frame_divider,
                         outer_width=outer_width,
                         html_px_size=html_px_size,
                         html_text_size=html_text_size,
                         html_outer_width=html_outer_width,
                         html_css_injection=html_css_injection)

        copied_lists = []
        for tablate_item in tablate_set:
            copied_lists = [*copied_lists, *deepcopy(tablate_item._frame_list)]
        self._frame_list = copied_lists
