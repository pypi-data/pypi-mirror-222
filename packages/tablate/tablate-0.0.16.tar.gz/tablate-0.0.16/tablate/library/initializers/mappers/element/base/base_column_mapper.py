from typing import Optional

from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.type.defaults import column_divider_default, background_default, column_padding_default
from tablate.type.type_base import ColumnBase
from tablate.type.type_store import ColumnStore


def base_column_mapper(columns_input: Optional[ColumnBase] = None,
                       column_defaults: Optional[ColumnBase] = None) -> ColumnStore:
    if columns_input is None:
        columns_input = ColumnBase()

    columns_return = ColumnStore(divider=set_attr_resolver(instance=columns_input,
                                                           key="divider",
                                                           default=set_attr_resolver(instance=column_defaults,
                                                                                     key="divider",
                                                                                     default=column_divider_default)),
                                 padding=set_attr_resolver(instance=columns_input,
                                                           key="padding",
                                                           default=set_attr_resolver(instance=column_defaults,
                                                                                     key="padding",
                                                                                     default=column_padding_default)))

    return columns_return
