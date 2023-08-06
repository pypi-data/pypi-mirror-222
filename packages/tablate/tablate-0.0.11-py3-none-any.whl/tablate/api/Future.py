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


########################################################################################################################
########################################################################################################################
########################################################################################################################


column_list: List[Union[GridColumnInput, TableColumnInput]] = [
    {
        "string": "Column One",
        "key": "Key One",
        "width": "50%",
        "divider": "thick",
        "background": "blue"
    },
    {
        "string": "Column Two",
        "key": "Key Two",
        "text_align": "right",
        "divider": "double"

    },
    {
        "string": "Column Three",
        "key": "Key Three",
        "text_align": "right"
    }
]

column_list2: List[Union[GridColumnInput, TableColumnInput]] = [
    {
        "string": "Column One",
        "key": "Key One",
        "width": "25%",
        "divider": "thick",
        "background": "blue"
    },
    {
        "string": "Column Two",
        "key": "Key Two",
        "text_align": "right",
        "divider": "double"

    },
    {
        "string": "Column Three",
        "key": "Key Three",
        "text_align": "right"
    }
]

row_list = [
    {
        "Key One": "Some string value",
        "Key Two": 4,
        "Key Three": 9.6,
        "divider": "thick"
    },
    {
        "Key One": "Some other string value",
        "Key Two": 5,
        "Key Three": 4.6

    },
    {
        "Key One": "Some final string value",
        "Key Two": 100,
        "Key Three": 328.832

    }
]
########################################################################################################################
html_global_styles_input = HtmlOuterBase(html_outer_border_style="thick",
                                         html_outer_padding=16,
                                         html_outer_width="100%")
########################################################################################################################
frame_styles_input = FrameStylesInput(frame_divider="thick",
                                      max_lines=None,
                                      multiline=True,
                                      background="yellow",
                                      trunc_value="...")
column_styles_input = ColumnStylesInput(divider="thick",
                                        padding=1)
text_styles_input = TextStylesInput(text_style="bold",
                                    text_align="left",
                                    text_color="green")
########################################################################################################################
html_frame_styles_input = HtmlFrameStylesInput(html_frame_divider_style="thick",
                                               html_max_lines=5,
                                               html_multiline=True,
                                               html_background="green")
html_column_styles_input = HtmlColumnStylesInput(html_divider_style="thin",
                                                 html_padding=6)
html_text_styles_input = HtmlTextStylesInput(html_text_style="normal",
                                             html_text_align="left",
                                             html_text_color="red",
                                             html_text_size=16)
########################################################################################################################
table_rows_frame_styles_input = TableBodyFrameStylesInput(frame_styles=frame_styles_input,
                                                          column_styles=column_styles_input,
                                                          text_styles=text_styles_input,
                                                          row_styles=TableRowsBase(row_line_divider="thin",
                                                                                   odds_background="grey",
                                                                                   evens_background="green"))
header_frame_styles_input = TableHeaderFrameStylesInput(frame_styles=frame_styles_input,
                                                        column_styles=column_styles_input,
                                                        text_styles=text_styles_input)
html_header_styles_input = HtmlTableHeaderFrameStylesInput(html_frame_styles=html_frame_styles_input,
                                                           html_column_styles=html_column_styles_input,
                                                           html_text_styles=html_text_styles_input)
html_rows_styles_input = HtmlTableBodyFrameStylesInput(html_frame_styles=html_frame_styles_input,
                                                       html_column_styles=html_column_styles_input,
                                                       html_text_styles=html_text_styles_input,
                                                       html_row_styles=HtmlTableRowsBase(
                                                           html_row_line_divider_style="none"
                                                       ))
########################################################################################################################

start = time.perf_counter_ns()
test = Tablate()
# test = Tablate(outer_border="thin",
#                      outer_padding=6,
#                      outer_width=120,
#                      html_outer_styles=html_global_styles_input,
#                      frame_divider="double",
#                      background="blue",
#                      column_styles=column_styles_input,
#                      text_styles=text_styles_input,
#                      html_frame_styles=html_frame_styles_input,
#                      html_column_styles=html_column_styles_input,
#                      html_text_styles=html_text_styles_input)

test.add_text_frame(text="Some String...",
                    text_style="bold",
                    text_align="left",
                    text_color="red",
                    frame_divider="thick",
                    background="blue",
                    multiline=True,
                    max_lines=5)

test.add_grid_frame(columns=column_list,
                    frame_divider="thick",
                    text_color="white",
                    text_style="bold_underlined",
                    background="dark_red",
                    multiline=True,
                    max_lines=5)

test.add_table_frame(columns=column_list,
                     rows=row_list,
                     odd_row_background="red",
                     text_color="yellow")

test.add_grid_frame(columns=column_list)

test.add_table_frame(columns=column_list,
                     rows=row_list,
                     name="Some Table",
                     frame_divider="thick",
                     background="blue",
                     multiline=True,
                     max_lines=5,
                     multiline_header=False,
                     max_lines_header=None,
                     hide_header=False,

                     column_divider="thin",
                     column_padding=1,
                     header_base_divider="thick",
                     row_line_divider="thin",
                     even_row_background="magenta",
                     odd_row_background="blue",

                     text_style="bold",
                     text_align="center",
                     text_color="blue",

                     header_styles=header_frame_styles_input,
                     body_styles=table_rows_frame_styles_input,

                     html_styles=html_rows_styles_input,

                     html_header_styles=html_header_styles_input,
                     html_body_styles=html_rows_styles_input)


test.add_text_frame(text="Some String...")

test.add_grid_frame(columns=column_list)

test.add_table_frame(columns=column_list2,
                     rows=row_list,
                     hide_header=True)

test.add_grid_frame(columns=column_list, html_px_multiplier=3, text_color="blue")

test.add_table_frame(columns=column_list,
                     rows=row_list,
                     text_color="grey")


string = test.to_string()
html = test.to_html()
print(string)
print(html)

test.list_frames()

test.get_frame(9).print()
