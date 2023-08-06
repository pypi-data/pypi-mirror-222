from typing import List, Union

from tablate.classes.bases.TablateApiBase import TablateApi
from tablate.library.initializers.grid_init import grid_init
from tablate.type.primitives import FrameDivider, ColumnDivider, OuterBorder, OuterPadding, OuterWidth, Background, \
    BackgroundPadding, HtmlPxMultiplier, Multiline, MaxLines, ColumnPadding, TextStyle, TextAlign, TextColor, FrameName
from tablate.type.type_input import GridColumnInput, HtmlOuterStylesInput, HtmlGridFrameStylesInput


class Grid(TablateApi):

    def __init__(self,
                 # TablateGrid args
                 columns: List[Union[str, GridColumnInput]],
                 name: FrameName = None,
                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,
                 multiline: Multiline = None,
                 max_lines: MaxLines = None,
                 column_divider: ColumnDivider = None,
                 column_padding: ColumnPadding = None,
                 text_style: TextStyle = None,
                 text_align: TextAlign = None,
                 text_color: TextColor = None,
                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlGridFrameStylesInput = None,
                 # TablateApi args
                 outer_border: OuterBorder = None,
                 outer_padding: OuterPadding = None,
                 outer_width: OuterWidth = None,
                 html_outer_styles: HtmlOuterStylesInput = None) -> None:
        super().__init__(outer_border=outer_border,
                         outer_padding=outer_padding,
                         frame_divider=frame_divider,
                         outer_width=outer_width,
                         html_styles=html_outer_styles)

        grid_dict = grid_init(columns=columns,
                              name=name,
                              frame_divider=frame_divider,
                              background=background,
                              background_padding=background_padding,
                              multiline=multiline,
                              max_lines=max_lines,
                              column_divider=column_divider,
                              column_padding=column_padding,
                              text_style=text_style,
                              text_align=text_align,
                              text_color=text_color,
                              html_px_multiplier=html_px_multiplier,
                              html_styles=html_styles,
                              options=self._options)

        self._frame_list.append(grid_dict)
