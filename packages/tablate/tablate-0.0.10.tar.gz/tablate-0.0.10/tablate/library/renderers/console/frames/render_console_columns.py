from typing import List

from tablate.library.ascii.chars.line_v import v_line
from tablate.library.checkers.is_last_element import is_last_element
from tablate.library.formatters.console.cell_string import cell_string_single_line
from tablate.library.formatters.console.row_outer_border import row_outer_border
from tablate.type.type_store import FrameStoreUnion
from tablate.type.type_global import Options


def column_console_multiline(formatted_columns_array: List[List[str]], frame_dict: FrameStoreUnion, options: Options):
    line_count = 0

    for column_item in formatted_columns_array:
        line_count = len(column_item) if len(column_item) > line_count else line_count

    line_count = line_count if frame_dict.frame_styles.max_lines is None \
                               or frame_dict.frame_styles.max_lines > line_count else frame_dict.frame_styles.max_lines

    return_string = ""

    for grid_line_index in range(line_count):
        grid_line_string = ""
        for column_index, column_item in enumerate(frame_dict.column_list):
            if grid_line_index < len(formatted_columns_array[column_index]):
                grid_line_string += formatted_columns_array[column_index][grid_line_index]
            else:
                grid_line_string += cell_string_single_line(string=column_item["string"],
                                                            column_item=column_item,
                                                            trunc_value=frame_dict.frame_styles.trunc_value)
            if not is_last_element(column_index, frame_dict.column_list):
                grid_line_string += v_line[column_item["divider"]]
        return_string += row_outer_border(row_string=grid_line_string, options=options)

    return return_string
