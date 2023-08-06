from typing import Union, Optional

from tablate.classes.bases.TablateApiBase import TablateApi
from tablate.library.initializers.text_init import text_init
from tablate.type.primitives import TextAlign, FrameDivider, OuterBorder, FrameName, TextStyle, TextColor, Background, \
    BackgroundPadding, Multiline, MaxLines, HtmlPxMultiplier, OuterPadding, OuterWidth, ColumnPadding
from tablate.type.type_input import HtmlTextFrameStylesInput, HtmlOuterStylesInput


class Text(TablateApi):

    def __init__(self,
                 # TablateText args
                 text: Union[str, int, float],

                 name: FrameName = None,

                 text_style: TextStyle = None,
                 text_align: TextAlign = None,
                 text_color: TextColor = None,
                 frame_padding: ColumnPadding = None,
                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,
                 multiline: Multiline = None,
                 max_lines: MaxLines = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlTextFrameStylesInput = None,
                 # TablateApi arge
                 outer_border: OuterBorder = None,
                 outer_padding: OuterPadding = None,
                 outer_width: OuterWidth = None,
                 html_outer_styles: HtmlOuterStylesInput = None) -> None:
        TablateApi.__init__(self=self,
                            outer_border=outer_border,
                            outer_padding=outer_padding,
                            frame_divider=frame_divider,
                            outer_width=outer_width,
                            html_styles=html_outer_styles)

        text_dict = text_init(text=text,
                              name=name,
                              text_style=text_style,
                              text_align=text_align,
                              text_color=text_color,
                              frame_divider=frame_divider,
                              frame_padding=frame_padding,
                              background=background,
                              background_padding=background_padding,
                              multiline=multiline,
                              max_lines=max_lines,
                              html_px_multiplier=html_px_multiplier,
                              html_styles=html_styles,
                              options=self._options)

        self._frame_list.append(text_dict)
