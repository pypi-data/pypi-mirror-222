from typing import List, Union

from tablate.classes.bases.TablateApi import TablateApi
from tablate.library.initializers.grid_init import grid_init
from tablate.type.primitives import FrameDivider, ColumnDivider, OuterBorder
from tablate.type.type_input import GridColumnInput


class Grid(TablateApi):

    def __init__(self,
                 # TablateGrid args
                 columns: List[Union[str, GridColumnInput]],
                 column_padding: int = 1,
                 column_divider: ColumnDivider = "thin",
                 frame_divider: FrameDivider = "thick",  # todo: doesn't make sense here
                 multiline: bool = True,
                 max_lines: int = None,
                 trunc_value: str = "...",
                 # TablateApi args
                 outer_border: OuterBorder = "thick",
                 outer_padding: int = 1,
                 outer_width: int = None,
                 html_px_size: int = 6,
                 html_text_size: int = 12,
                 html_outer_width: str = "100%",
                 html_css_injection: str = "") -> None:

        TablateApi.__init__(self=self,
                            outer_border=outer_border,
                            outer_padding=outer_padding,
                            frame_divider=frame_divider,
                            outer_width=outer_width,
                            html_px_size=html_px_size,
                            html_text_size=html_text_size,
                            html_outer_width=html_outer_width,
                            html_css_injection=html_css_injection)

        grid_dict = grid_init(columns=columns,
                              column_padding=column_padding,
                              column_divider=column_divider,
                              frame_divider=frame_divider,
                              multiline=multiline,
                              max_lines=max_lines,
                              trunc_value=trunc_value,
                              outer_width=self._options["console"]["outer_width"])

        self._frame_list.append(grid_dict)