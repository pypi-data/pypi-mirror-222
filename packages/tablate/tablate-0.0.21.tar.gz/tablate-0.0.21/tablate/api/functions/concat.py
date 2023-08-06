from typing import List

from tablate.classes.bases.TablateSet import TablateSet
from tablate.type.primitives import FrameDivider, OuterBorder, OuterPadding, OuterWidth, Background, BackgroundPadding, \
    HtmlPxMultiplier
from tablate.type.type_input import HtmlOuterStylesInput, ColumnStylesInput, TextStylesInput, HtmlFrameStylesInput, \
    HtmlColumnStylesInput, HtmlTextStylesInput


def concat(frame_list: dict,
           outer_border: OuterBorder = None,
           outer_padding: OuterPadding = None,
           outer_width: OuterWidth = None,

           frame_divider: FrameDivider = None,
           background: Background = None,
           background_padding: BackgroundPadding = None,

           html_px_multiplier: HtmlPxMultiplier = None,
           html_styles: HtmlOuterStylesInput = None,

           column_styles: ColumnStylesInput = None,
           text_styles: TextStylesInput = None,

           html_frame_styles: HtmlFrameStylesInput = None,

           html_column_styles: HtmlColumnStylesInput = None,
           html_text_styles: HtmlTextStylesInput = None):

    return TablateSet(**locals())
