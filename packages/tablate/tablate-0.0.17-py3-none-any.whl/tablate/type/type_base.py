from dataclasses import dataclass, field
from typing import Optional

from tablate.type.primitives import FrameDivider, OuterBorder, TextStyle, TextAlign, ColumnWidth, \
    ColumnPadding, MaxLines, Multiline, OuterWidth, OuterPadding, HtmlTextStyle, HtmlTextColor, HtmlTextSize, \
    HtmlColumnDividerStyle, HtmlColumnPadding, HtmlBackground, HtmlFrameDivider, \
    HtmlPxMultiplier, HtmlOuterBorder, HtmlOuterPadding, HtmlOuterWidth, HtmlTextAlign, Background, TextColor, \
    TruncValue, TextString, TableRowKey, ColumnDivider, HtmlDividerWeight, BackgroundPadding


@dataclass
class OuterBase:
    outer_border: Optional[OuterBorder] = None
    outer_padding: Optional[OuterPadding] = None
    outer_width: Optional[OuterWidth] = None


###################################

@dataclass
class FrameBase:
    frame_divider: Optional[FrameDivider] = None
    max_lines: Optional[MaxLines] = None
    multiline: Optional[Multiline] = None
    background: Optional[Background] = None
    trunc_value: Optional[TruncValue] = None


@dataclass
class ColumnBase:
    divider: Optional[ColumnDivider] = None
    padding: Optional[ColumnPadding] = None
    background_padding: Optional[BackgroundPadding] = None


@dataclass
class TextBase:
    text_style: Optional[TextStyle] = None
    text_align: Optional[TextAlign] = None
    text_color: Optional[TextColor] = None


###################################
###################################
###################################

TableHeaderFrameBase = FrameBase


@dataclass
class TableRowsBase:
    row_line_divider: Optional[FrameDivider] = None
    odds_background: Optional[Background] = None
    evens_background: Optional[Background] = None


########################################################################################################################
########################################################################################################################
########################################################################################################################

@dataclass
class HtmlOuterBase:
    html_outer_border_weight: Optional[HtmlDividerWeight] = None
    html_outer_border_style: Optional[HtmlOuterBorder] = None
    html_outer_padding: Optional[HtmlOuterPadding] = None
    html_outer_width: Optional[HtmlOuterWidth] = None

@dataclass
class HtmlFrameBase:
    html_frame_divider_style: Optional[HtmlFrameDivider] = None
    html_frame_divider_weight: Optional[HtmlDividerWeight] = None
    html_max_lines: Optional[MaxLines] = None
    html_multiline: Optional[Multiline] = None
    html_background: Optional[HtmlBackground] = None


@dataclass
class HtmlColumnBase:
    html_divider_style: Optional[HtmlColumnDividerStyle] = None
    html_divider_weight: Optional[HtmlDividerWeight] = None
    html_padding: Optional[HtmlColumnPadding] = None


@dataclass
class HtmlTextBase:
    html_text_style: Optional[HtmlTextStyle] = None
    html_text_align: Optional[HtmlTextAlign] = None
    html_text_color: Optional[HtmlTextColor] = None
    html_text_size: Optional[HtmlTextSize] = None


###################################
###################################
###################################


@dataclass
class HtmlTableRowsBase:
    html_row_line_divider_weight: Optional[HtmlDividerWeight] = None
    html_row_line_divider_style: Optional[HtmlFrameDivider] = None
    html_odds_background: Optional[HtmlBackground] = None
    html_evens_background: Optional[HtmlBackground] = None



