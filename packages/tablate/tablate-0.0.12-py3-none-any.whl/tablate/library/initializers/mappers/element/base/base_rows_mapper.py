from typing import Optional

from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.type.defaults import row_line_divider_default, background_default
from tablate.type.type_base import TableRowsBase
from tablate.type.type_store import TableRowsStore


def base_rows_mapper(base_rows_input: Optional[TableRowsBase] = None,
                     rows_defaults: Optional[TableRowsBase] = None) -> TableRowsStore:
    row_line_divider = set_attr_resolver(instance=base_rows_input,
                                         key="row_line_divider",
                                         default=set_attr_resolver(instance=rows_defaults,
                                                                   key="row_line_divider",
                                                                   default=row_line_divider_default))
    odds_background = set_attr_resolver(instance=base_rows_input,
                                        key="odds_background",
                                        default=set_attr_resolver(instance=rows_defaults,
                                                                  key="odds_background",
                                                                  default=background_default))
    evens_background = set_attr_resolver(instance=base_rows_input,
                                         key="evens_background",
                                         default=set_attr_resolver(instance=rows_defaults,
                                                                   key="odds_background",
                                                                   default=background_default))

    rows_return = TableRowsStore(row_line_divider=row_line_divider,
                                 odds_background=odds_background,
                                 evens_background=evens_background)

    return rows_return
