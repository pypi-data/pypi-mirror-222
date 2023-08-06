from typing import Literal, Union, Optional, Tuple, List

Colors = Optional[Literal[
    # "inverted",
    "white",
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "dark_red",
    "dark_green",
    "dark_yellow",
    "dark_blue",
    "dark_magenta",
    "dark_cyan",
    "dark_grey",
    "black",
]]

# todo: implement inverted colour

TextString = Union[str, int, float]
TableRowKey = str

TextAlign = Optional[Literal["left", "center", "right"]]
TextStyle = Optional[Literal["normal", "bold", "underlined", "bold_underlined"]]
TextColor = Colors

HeaderAlignment = Literal["column", "left", "center", "right"]

OuterBorder = Literal["blank", "thin", "thick", "double"]
FrameDivider = Literal["none", "blank", "thin", "thick", "double"]
ColumnDivider = Literal["blank", "thin", "thick", "double"]

HeaderColumnDivider = Literal["rows", "blank", "thin", "thick", "double"]

HideHeader = bool

CharInteger = int
PercentString = str

ColumnWidth = Optional[Union[CharInteger, PercentString]]
ColumnPadding = CharInteger
Background = Colors
BackgroundPadding = int

MaxLines = Optional[int]
Multiline = Optional[bool]
TruncValue = str

OuterPadding = CharInteger
OuterWidth = CharInteger

CssStyleBlock = str
CssString = str
CssColor = str
PxInteger = int

HtmlPxMultiplier = int

# HtmlBorder = Tuple[Literal["none", "solid", "double"], PxInteger, CssColor]
HtmlBorder = Literal["none", "thin", "thick", "double"]
HtmlPadding = Union[PxInteger, List[int]]

HtmlTextStyle = Optional[Literal["normal", "bold", "italic"]]
HtmlTextAlign = Optional[Literal["left", "center", "right", "justify"]]
HtmlTextColor = Optional[CssColor]
HtmlTextSize = Optional[PxInteger]

# HtmlColumnWidth = Optional[PercentString]

HtmlDividerWeight = Optional[PxInteger]
HtmlColumnDividerStyle = Optional[HtmlBorder]
HtmlColumnPadding = Optional[HtmlPadding]
HtmlBackground = Optional[CssColor]

HtmlFrameDivider = Optional[HtmlBorder]

HtmlOuterBorder = Optional[HtmlBorder]
HtmlOuterPadding = Optional[HtmlPadding]
HtmlOuterWidth = Optional[PercentString]  # this will be a calc % - padding

HtmlFrameType = Literal["head", "body"]

HtmlRowGroupElement = Literal["tbody", "thead"]

HtmlCellElement = Literal["td", "th"]

y: tuple[str, str] = ("hi", "world")

