from typing import Union

from tablate.api.modules.Grid import Grid
from tablate.api.modules.Table import Table
from tablate.api.modules.Text import Text
from tablate.type.type_global import Options
from tablate.type.type_input import TableHeaderFrameStylesInput, HtmlTableHeaderFrameStylesInput, \
    TableBodyFrameStylesInput, HtmlTableBodyFrameStylesInput, HtmlTableFrameStylesInput, HtmlGridFrameStylesInput, \
    HtmlTextFrameStylesInput
from tablate.type.type_store import FrameStoreUnion, FrameStoreList


def get_frame(frame_list: FrameStoreList, options: Options, selector: Union[int, str]):
    selector_index = 0
    for frame_index, frame_item in enumerate(frame_list):
        if frame_item.type == "table_header":
            continue
        if (type(selector) == int and selector == selector_index) or (
                type(selector) == str and selector == frame_item.name):
            if frame_item.type == "text":
                print("here", "text")
                return Text(text=frame_item.column_list[0]["string"],
                            name=frame_item.name,
                            text_style=frame_item.text_styles.text_style,
                            text_align=frame_item.text_styles.text_align,
                            text_color=frame_item.text_styles.text_color,
                            frame_divider=frame_item.frame_styles.frame_divider,
                            background=frame_item.frame_styles.background,
                            background_padding=frame_item.column_list[0]["background_padding"],
                            multiline=frame_item.frame_styles.multiline,
                            max_lines=frame_item.frame_styles.max_lines,

                            html_px_multiplier=frame_item.html_frame_styles.html_px_multiplier,
                            html_styles=HtmlTextFrameStylesInput(html_frame_styles=frame_item.html_frame_styles,
                                                                 html_text_styles=frame_item.html_text_styles),
                            # TablateApi arge
                            outer_border=options.console.outer_styles.outer_border,
                            outer_padding=options.console.outer_styles.outer_padding,
                            outer_width=options.console.outer_styles.outer_width,
                            html_outer_styles=options.html.html_outer_styles)
            if frame_item.type == "grid":
                print("here", "grid")
                return Grid(columns=frame_item.column_list,
                            name=frame_item.name,
                            frame_divider=frame_item.frame_styles.frame_divider,
                            background=frame_item.frame_styles.background,
                            background_padding=frame_item.column_styles.background_padding,
                            multiline=frame_item.frame_styles.multiline,
                            max_lines=frame_item.frame_styles.max_lines,
                            column_divider=frame_item.column_styles.divider,
                            column_padding=frame_item.column_styles.padding,
                            text_style=frame_item.text_styles.text_style,
                            text_align=frame_item.text_styles.text_align,
                            text_color=frame_item.text_styles.text_color,
                            html_px_multiplier=frame_item.html_frame_styles.html_px_multiplier,
                            html_styles=HtmlGridFrameStylesInput(html_frame_styles=frame_item.html_frame_styles,
                                                                 html_column_styles=frame_item.html_column_styles,
                                                                 html_text_styles=frame_item.html_text_styles),
                            # TablateApi args
                            outer_border=options.console.outer_styles.outer_border,
                            outer_padding=options.console.outer_styles.outer_padding,
                            outer_width=options.console.outer_styles.outer_width,
                            html_outer_styles=options.html.html_outer_styles)
            elif frame_item.type == "table_body":
                print("here", "table")
                header_base_divider = None
                header_styles = None
                html_header_styles = None
                if frame_item.hide_header is False:
                    header_frame = frame_list[frame_index - 1]
                    header_base_divider = header_frame.frame_styles.frame_divider
                    header_styles = TableHeaderFrameStylesInput(frame_styles=header_frame.frame_styles,
                                                                column_styles=header_frame.column_styles,
                                                                text_styles=header_frame.text_styles)
                    html_header_styles = HtmlTableHeaderFrameStylesInput(
                        html_frame_styles=header_frame.html_frame_styles,
                        html_column_styles=header_frame.html_column_styles,
                        html_text_styles=header_frame.html_text_styles)
                return Table(columns=frame_item.column_list,
                             rows=frame_item.row_list,
                             name=frame_item.name,
                             frame_divider=frame_item.frame_styles.frame_divider,
                             background=frame_item.frame_styles.background,
                             background_padding=frame_item.column_styles.background_padding,
                             multiline=frame_item.frame_styles.multiline,
                             max_lines=frame_item.frame_styles.max_lines,
                             column_divider=frame_item.column_styles.divider,
                             column_padding=frame_item.column_styles.padding,
                             text_style=frame_item.text_styles.text_style,
                             text_align=frame_item.text_styles.text_align,
                             text_color=frame_item.text_styles.text_color,
                             header_base_divider=header_base_divider,
                             hide_header=frame_item.hide_header,
                             row_line_divider=frame_item.row_styles.row_line_divider,
                             odd_row_background=frame_item.row_styles.odds_background,
                             even_row_background=frame_item.row_styles.evens_background,
                             html_px_multiplier=frame_item.html_frame_styles.html_px_multiplier,
                             header_styles=header_styles,
                             body_styles=TableBodyFrameStylesInput(frame_styles=frame_item.frame_styles,
                                                                   column_styles=frame_item.column_styles,
                                                                   text_styles=frame_item.text_styles,
                                                                   row_styles=frame_item.row_styles),
                             html_header_styles=html_header_styles,
                             html_body_styles=HtmlTableBodyFrameStylesInput(
                                 html_frame_styles=frame_item.html_frame_styles,
                                 html_column_styles=frame_item.html_column_styles,
                                 html_text_styles=frame_item.html_text_styles,
                                 html_row_styles=frame_item.html_row_styles),
                             html_styles=HtmlTableFrameStylesInput(html_frame_styles=frame_item.html_frame_styles,
                                                                   html_column_styles=frame_item.html_column_styles,
                                                                   html_text_styles=frame_item.html_text_styles,
                                                                   html_row_styles=frame_item.html_row_styles),
                             # TablateApi args
                             outer_border=options.console.outer_styles.outer_border,
                             outer_padding=options.console.outer_styles.outer_padding,
                             outer_width=options.console.outer_styles.outer_width,
                             html_outer_styles=options.html.html_outer_styles)
        selector_index += 1
