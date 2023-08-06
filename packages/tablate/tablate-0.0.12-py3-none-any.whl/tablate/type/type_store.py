from dataclasses import dataclass
from typing import Literal, Union, List, Dict

from tablate.type.primitives import TextString, TableRowKey, HtmlPxMultiplier, BackgroundPadding, FrameName, HideHeader
from tablate.type.type_base import ColumnBase, TextBase, HtmlTextBase, FrameBase, HtmlColumnBase, \
    HtmlTableRowsBase, TableRowsBase, HtmlFrameBase, HtmlOuterBase, OuterBase
from tablate.type.type_input import GridColumnInput, TableColumnInput, BaseColumnInput

########################################################################################################################
# FrameDicts ###########################################################################################################
########################################################################################################################


@dataclass
class OuterStore(OuterBase):
    background_padding: BackgroundPadding = None


@dataclass
class HtmlOuterStore(HtmlOuterBase):
    html_px_multiplier: HtmlPxMultiplier = None


@dataclass
class HtmlFrameStore(HtmlFrameBase):
    html_px_multiplier: HtmlPxMultiplier = None


FrameStore = FrameBase
ColumnStore = ColumnBase
TextStore = TextBase

HtmlColumnStore = HtmlColumnBase
HtmlTextStore = HtmlTextBase

TableRowsStore = TableRowsBase
HtmlTableRowsStore = HtmlTableRowsBase


class BaseColumnStore(BaseColumnInput):
    background_padding: BackgroundPadding


@dataclass
class BaseFrameStore:
    frame_styles: FrameStore
    column_styles: ColumnStore
    text_styles: TextStore
    html_frame_styles: HtmlFrameStore
    html_column_styles: HtmlColumnStore
    html_text_styles: HtmlTextStore


# Grid FrameDict #######################################################################################################


GridColumnStore = GridColumnInput


@dataclass()
class GridFrameStore(BaseFrameStore):
    type: Union[Literal["grid"], Literal["text"]]
    name: FrameName
    column_list: List[GridColumnStore]


# Table FrameDict ######################################################################################################

@dataclass()
class TableHeaderFrameStore(BaseFrameStore):
    type: Literal["table_header"]
    name: FrameName
    column_list: List[TableColumnInput]


@dataclass()
class TableBodyFrameStore(BaseFrameStore):
    type: Literal["table_body"]
    name: FrameName
    hide_header: HideHeader
    column_list: List[TableColumnInput]
    row_list: List[Dict[TableRowKey, TextString]]
    row_styles: TableRowsStore
    html_row_styles: HtmlTableRowsStore


# FrameDict List #######################################################################################################

FrameStoreUnion = Union[GridFrameStore, TableHeaderFrameStore, TableBodyFrameStore]
FrameStoreList = List[FrameStoreUnion]


