from shutil import get_terminal_size

from tablate.type.primitives import Colors, TextAlign, TextStyle, TextColor, HeaderAlignment, OuterBorder, \
    ColumnDivider, HeaderColumnDivider, HideHeader, ColumnWidth, ColumnPadding, Background, FrameDivider, \
    MaxLines, Multiline, TruncValue, OuterPadding, OuterWidth, HtmlTextStyle, HtmlTextAlign, \
    HtmlTextColor, HtmlTextSize, HtmlColumnDividerStyle, HtmlColumnPadding, HtmlBackground, \
    HtmlFrameDivider, HtmlPxMultiplier, HtmlOuterBorder, HtmlOuterPadding, HtmlOuterWidth, FrameName

global_text_align_default: TextAlign = None
global_text_style_default: TextStyle = None
global_multiline_default: Multiline = None

############################################################################################

frame_name_default: FrameName = ""

colors_default: Colors = None

text_align_default: TextAlign = "left"
text_style_default: TextStyle = "normal"
text_color_default: TextColor = None

outer_padding_default: OuterPadding = 1
outer_width_default: OuterWidth = get_terminal_size((120 + (outer_padding_default * 2), 0))[0] - (outer_padding_default * 2)

outer_border_default: OuterBorder = "thick"
frame_divider_default: FrameDivider = "thick"
column_divider_default: ColumnDivider = "thin"
row_line_divider_default: FrameDivider = "thin"

hide_header_default: HideHeader = False

column_width_default: ColumnWidth = None
column_padding_default: ColumnPadding = 1
background_default: Background = None
background_padding_default = 1

max_lines_default: MaxLines = None
multiline_default: Multiline = True
trunc_value_default: TruncValue = "..."

############################################################################################

header_base_divider_default = "thin"

table_multiline_default: Multiline = False

table_header_text_style_default: TextStyle = "bold"
table_header_text_align_default: HeaderAlignment = "column"
table_header_column_divider_default: HeaderColumnDivider = "rows"

############################################################################################

html_padding_default = 6
html_divider_weight_default = 1
html_text_size_default = 16
html_px_multiplier_default: HtmlPxMultiplier = 1
html_outer_width_default: HtmlOuterWidth = "100%"

# html_text_style_default: HtmlTextStyle = None
# html_text_align_default: HtmlTextAlign = None
# html_text_color_default: HtmlTextColor = None
# html_text_size_default: HtmlTextSize = None
#
# html_column_width_default: HtmlColumnWidth = None
# html_column_divider_default: HtmlColumnDivider = None
# html_column_padding_default: HtmlColumnPadding = None
# html_background_default: HtmlBackground = None
#
# html_frame_divider_default: HtmlFrameDivider = None
#
# html_outer_border_default: HtmlOuterBorder = None
# html_outer_padding_default: HtmlOuterPadding = None

