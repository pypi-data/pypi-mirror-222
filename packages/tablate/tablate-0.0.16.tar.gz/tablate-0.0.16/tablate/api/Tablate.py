import time
from typing import List, Union

from tablate.classes.bases.TablateApiBase import TablateApi
from tablate.classes.bases.TablateApiSet import TablateSet
from tablate.library.initializers.grid_init import grid_init
from tablate.library.initializers.table_init import table_init
from tablate.library.initializers.text_init import text_init
from tablate.type.primitives import OuterBorder, FrameDivider, OuterPadding, OuterWidth, Multiline, TextColor, \
    TextAlign, TextStyle, MaxLines, HideHeader, Background, ColumnDivider, ColumnPadding, HtmlPxMultiplier, \
    BackgroundPadding, FrameName
from tablate.type.type_base import HtmlOuterBase, HtmlTableRowsBase, TableRowsBase, TextBase
from tablate.type.type_input import GridColumnInput, TableHeaderFrameStylesInput, \
    TableBodyFrameStylesInput, HtmlTableBodyFrameStylesInput, HtmlTableHeaderFrameStylesInput, \
    HtmlTableFrameStylesInput, TableColumnInput, \
    HtmlTextStylesInput, HtmlColumnStylesInput, ColumnStylesInput, TextStylesInput, TableRowsDataInputDict, \
    HtmlFrameStylesInput, FrameStylesInput, HtmlOuterStylesInput, HtmlTextFrameStylesInput, \
    HtmlGridFrameStylesInput


class Tablate(TablateSet):

    def __init__(self,
                 outer_border: OuterBorder = None,
                 outer_padding: OuterPadding = None,
                 outer_width: OuterWidth = None,

                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_outer_styles: HtmlOuterStylesInput = None,

                 column_styles: ColumnStylesInput = None,
                 text_styles: TextStylesInput = None,

                 html_frame_styles: HtmlFrameStylesInput = None,
                 html_column_styles: HtmlColumnStylesInput = None,
                 html_text_styles: HtmlTextStylesInput = None) -> None:

        super().__init__(outer_border=outer_border,
                         outer_padding=outer_padding,
                         outer_width=outer_width,
                         frame_divider=frame_divider,
                         background=background,
                         background_padding=background_padding,
                         html_px_multiplier=html_px_multiplier,
                         html_styles=html_outer_styles,
                         column_styles=column_styles,
                         text_styles=text_styles,
                         html_frame_styles=html_frame_styles,
                         html_column_styles=html_column_styles,
                         html_text_styles=html_text_styles)

    def add_text_frame(self,
                       text: Union[str, int, float],

                       name: FrameName = None,

                       text_style: TextStyle = None,
                       text_align: TextAlign = None,
                       text_color: TextColor = None,

                       frame_divider: FrameDivider = None,
                       frame_padding: ColumnPadding = None,
                       background: Background = None,
                       background_padding: BackgroundPadding = None,
                       multiline: Multiline = None,
                       max_lines: MaxLines = None,

                       html_px_multiplier: HtmlPxMultiplier = None,
                       html_styles: HtmlTextFrameStylesInput = None) -> None:

        text_frame_store = text_init(text=text,
                                     name=name,
                                     frame_divider=frame_divider,
                                     frame_padding=frame_padding,
                                     background=background,
                                     background_padding=background_padding,
                                     multiline=multiline,
                                     max_lines=max_lines,
                                     text_style=text_style,
                                     text_align=text_align,
                                     text_color=text_color,
                                     html_px_multiplier=html_px_multiplier,
                                     html_styles=html_styles,
                                     options=self._options)

        self._frame_list.append(text_frame_store)

    def add_grid_frame(self,
                       columns: List[Union[str, GridColumnInput]],

                       name: FrameName = None,

                       frame_divider: FrameDivider = None,
                       background: Background = None,
                       background_padding: BackgroundPadding = None,
                       multiline: Multiline = None,
                       max_lines: MaxLines = None,

                       column_divider: ColumnDivider = None,
                       column_padding: ColumnPadding = None,

                       text_style: TextStyle = None,
                       text_align: TextAlign = None,
                       text_color: TextColor = None,

                       html_px_multiplier: HtmlPxMultiplier = None,
                       html_styles: HtmlGridFrameStylesInput = None) -> None:

        grid_frame_store = grid_init(columns=columns,
                                     name=name,
                                     frame_divider=frame_divider,
                                     background=background,
                                     background_padding=background_padding,
                                     multiline=multiline,
                                     max_lines=max_lines,
                                     column_divider=column_divider,
                                     column_padding=column_padding,
                                     text_style=text_style,
                                     text_align=text_align,
                                     text_color=text_color,
                                     html_styles=html_styles,
                                     html_px_multiplier=html_px_multiplier,
                                     options=self._options)

        self._frame_list.append(grid_frame_store)

    def add_table_frame(self,
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
                        html_body_styles: HtmlTableBodyFrameStylesInput = None) -> None:

        table_header_store, table_body_store = table_init(columns=columns,
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

        if table_header_store:
            self._frame_list.append(table_header_store)

        self._frame_list.append(table_body_store)

