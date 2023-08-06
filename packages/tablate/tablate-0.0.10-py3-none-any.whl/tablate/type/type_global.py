from dataclasses import dataclass
from typing import List, Optional

from tablate.classes.options.html.style.CssStyler import CssStyler
from tablate.type.primitives import CssStyleBlock, PxInteger
from tablate.type.type_base import HtmlOuterBase, FrameBase, ColumnBase, TextBase, OuterBase, HtmlFrameBase, \
    HtmlColumnBase, HtmlTextBase
from tablate.type.type_store import HtmlOuterStore, OuterStore


@dataclass
class ConsoleOptions:
    outer_styles: OuterStore
    frame_styles: FrameBase
    column_styles: ColumnBase
    text_styles: TextBase


@dataclass
class HtmlOptions:
    html_outer_styles: HtmlOuterStore
    html_frame_styles: HtmlFrameBase
    html_column_styles: HtmlColumnBase
    html_text_styles: HtmlTextBase
    css_injection: CssStyleBlock
    styler: Optional[CssStyler]
    column_baselines: List[PxInteger]


@dataclass
class Options:
    console: ConsoleOptions
    html: HtmlOptions
