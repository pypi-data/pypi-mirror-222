from typing import List, Dict, Union

from tablate.classes.bases.TablateApi import TablateApi
from tablate.library.initializers.table_init import table_init
from tablate.type.primitives import FrameDivider, ColumnDivider, HeaderAlignment, HeaderColumnDivider, OuterBorder
from tablate.type.type_input import TableColumnInput


class Table(TablateApi):

    def __init__(self,
                 # TablateTable args
                 columns: List[TableColumnInput],
                 rows: List[Dict[str, Union[str, int, float]]],
                 column_padding: int = None,
                 row_line_divider: FrameDivider = None,
                 row_column_divider: ColumnDivider = None,
                 frame_divider: FrameDivider = None,  # todo: doesn't make sense here
                 header_text_align: HeaderAlignment = None,
                 header_column_divider: HeaderColumnDivider = None,
                 header_frame_divider: FrameDivider = None,
                 multiline: bool = False,
                 max_lines: int = None,
                 multiline_header: bool = False,
                 max_lines_header: int = None,
                 hide_header: bool = False,
                 # TablateApi args
                 outer_border: OuterBorder = None,
                 outer_padding: int = None,
                 outer_width: int = None,
                 html_px_size: int = None,
                 html_text_size: int = None,
                 html_outer_width: str = None,
                 html_css_injection: str = "") -> None:

        TablateApi.__init__(self=self,
                            outer_border=outer_border,
                            outer_padding=outer_padding,
                            frame_divider=frame_divider,
                            outer_width=outer_width,
                            html_px_size=html_px_size,
                            html_text_size=html_text_size,
                            html_outer_width=html_outer_width,
                            html_css_injection=html_css_injection)

        table_head_dict, table_rows_dict = table_init(columns=columns,
                                                      rows=rows,
                                                      column_padding=column_padding,
                                                      row_line_divider=row_line_divider,
                                                      row_column_divider=row_column_divider,
                                                      frame_divider=frame_divider,
                                                      header_text_align=header_text_align,
                                                      header_column_divider=header_column_divider,
                                                      header_frame_divider=header_frame_divider,
                                                      multiline=multiline,
                                                      max_lines=max_lines,
                                                      multiline_header=multiline_header,
                                                      max_lines_header=max_lines_header,
                                                      hide_header=hide_header,
                                                      head_trunc_value="...",
                                                      row_trunc_value="...",
                                                      outer_width=self._options["console"]["outer_width"])

        if table_head_dict:
            self._frame_list.append(table_head_dict)

        self._frame_list.append(table_rows_dict)
