from typing import List, Dict, Union

from tablate.classes.bases.TablateApiBase import TablateApi
from tablate.library.initializers.table_init import table_init
from tablate.type.primitives import FrameDivider, ColumnDivider, HeaderAlignment, HeaderColumnDivider, OuterBorder, \
    FrameName, Multiline, MaxLines, Background, BackgroundPadding, HideHeader, ColumnPadding, TextAlign, TextStyle, \
    TextColor, HtmlPxMultiplier, OuterPadding, OuterWidth
from tablate.type.type_input import TableColumnInput, TableRowsDataInputDict, TableBodyFrameStylesInput, \
    TableHeaderFrameStylesInput, HtmlTableFrameStylesInput, HtmlTableHeaderFrameStylesInput, \
    HtmlTableBodyFrameStylesInput, HtmlOuterStylesInput


class Table(TablateApi):

    def __init__(self,
                 # TablateTable args
                 columns: List[TableColumnInput],
                 rows: List[TableRowsDataInputDict],

                 name: FrameName = None,

                 frame_divider: FrameDivider = None,
                 multiline: Multiline = None,
                 max_lines: MaxLines = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,

                 multiline_header: Multiline = None,
                 max_lines_header: MaxLines = None,
                 hide_header: HideHeader = None,

                 column_divider: ColumnDivider = None,
                 column_padding: ColumnPadding = None,
                 header_base_divider: FrameDivider = None,

                 row_line_divider: FrameDivider = None,
                 odd_row_background: Background = None,
                 even_row_background: Background = None,

                 text_style: TextStyle = None,
                 text_align: TextAlign = None,
                 text_color: TextColor = None,

                 header_styles: TableHeaderFrameStylesInput = None,
                 body_styles: TableBodyFrameStylesInput = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlTableFrameStylesInput = None,

                 html_header_styles: HtmlTableHeaderFrameStylesInput = None,
                 html_body_styles: HtmlTableBodyFrameStylesInput = None,

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

        table_head_dict, table_rows_dict = table_init(columns=columns,
                                                      rows=rows,
                                                      name=name,
                                                      frame_divider=frame_divider,
                                                      multiline=multiline,
                                                      max_lines=max_lines,
                                                      background=background,
                                                      background_padding=background_padding,
                                                      multiline_header=multiline_header,
                                                      max_lines_header=max_lines_header,
                                                      hide_header=hide_header,
                                                      column_divider=column_divider,
                                                      column_padding=column_padding,
                                                      header_base_divider=header_base_divider,
                                                      row_line_divider=row_line_divider,
                                                      odd_row_background=odd_row_background,
                                                      even_row_background=even_row_background,
                                                      text_style=text_style,
                                                      text_align=text_align,
                                                      text_color=text_color,
                                                      header_styles=header_styles,
                                                      body_styles=body_styles,
                                                      html_px_multiplier=html_px_multiplier,
                                                      html_styles=html_styles,
                                                      html_header_styles=html_header_styles,
                                                      html_body_styles=html_body_styles,
                                                      options=self._options)
        if table_head_dict:
            self._frame_list.append(table_head_dict)

        self._frame_list.append(table_rows_dict)
