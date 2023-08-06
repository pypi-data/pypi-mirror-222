from tablate.library.ascii.chars.line_h import h_line
from tablate.library.ascii.chars.line_v import v_line
from tablate.library.ascii.chars.matrix_cross import cross_matrix
from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.library.formatters.console.ascii_styler import ascii_text_styler, ascii_terminator
from tablate.library.formatters.console.concat_string import concat_string
from tablate.type.type_store import FrameStoreList


def list_frames(frame_list: FrameStoreList):
    print()
    # top_index = f"{' '}{h_line['thin'] * ((len(frame_list) // 10) + 3)}{cross_matrix['blank']['thin']['thin']}"
    # top_name = f"{h_line['thin'] * 22}{cross_matrix['blank']['thin']['thin']}"
    # top_type = f"{h_line['thin'] * 8}{cross_matrix['blank']['thin']['thin']}"
    # top_cols = f"{h_line['thin'] * 7}{cross_matrix['blank']['thin']['thin']}"
    # top_rows = f"{h_line['thin'] * 7}{cross_matrix['blank']['thin']['thin']}"
    # top_options = f"{h_line['thin'] * 42}"
    # print(f"{top_index}{top_name}{top_type}{top_cols}{top_rows}{top_options}")
    divider = v_line["thin"]
    padding = " "
    header_string = f"{padding} {' ' * ((len(frame_list) // 10) + 1)}{padding}"
    frame_name, name_ws = concat_string(string="Name",
                                        width=20,
                                        padding=0,
                                        trunc_value="")
    frame_name = ascii_text_styler(string=frame_name, column_dict={"text_style": "bold"}) + ascii_terminator()
    header_string += f"{divider}{padding}{frame_name}{' ' * name_ws}{padding}"
    frame_type, type_ws = concat_string(string="Type",
                                        width=6,
                                        padding=0,
                                        trunc_value="")
    frame_type = ascii_text_styler(string=frame_type, column_dict={"text_style": "bold"}) + ascii_terminator()
    header_string += f"{divider}{padding}{frame_type}{' ' * type_ws}{padding}"
    frame_cols, cols_ws = concat_string(string="Cols.",
                                        width=5,
                                        padding=0,
                                        trunc_value="")
    frame_cols = ascii_text_styler(string=frame_cols, column_dict={"text_style": "bold"}) + ascii_terminator()
    header_string += f"{divider}{padding}{frame_cols}{' ' * cols_ws}{padding}"
    frame_rows, rows_ws = concat_string(string="Rows",
                                        width=5,
                                        padding=0,
                                        trunc_value="")
    frame_rows = ascii_text_styler(string=frame_rows, column_dict={"text_style": "bold"}) + ascii_terminator()
    header_string += f"{divider}{padding}{' ' * rows_ws}{frame_rows}{padding}"
    frame_options = ascii_text_styler(string="Options", column_dict={"text_style": "bold"}) + ascii_terminator()
    header_string += f"{divider}{padding}{frame_options}{padding}"
    print(header_string)
    divider_index = f"{padding}{h_line['thin'] * ((len(frame_list) // 10) + 3)}{cross_matrix['thin']['thin']['thin']}"
    divider_name = f"{h_line['thin'] * 22}{cross_matrix['thin']['thin']['thin']}"
    divider_type = f"{h_line['thin'] * 8}{cross_matrix['thin']['thin']['thin']}"
    divider_cols = f"{h_line['thin'] * 7}{cross_matrix['thin']['thin']['thin']}"
    divider_rows = f"{h_line['thin'] * 7}{cross_matrix['thin']['thin']['thin']}"
    divider_options = f"{h_line['thin'] * 42}"
    print(f"{divider_index}{divider_name}{divider_type}{divider_cols}{divider_rows}{divider_options}")
    frame_index = 0
    for frame_item in frame_list:
        if frame_item.type == "table_header":
            continue
        item_string = f"{padding}"
        index, index_ws = concat_string(string=frame_index,
                                        width=(len(frame_list) // 10) + 1,
                                        padding=0,
                                        trunc_value="")
        item_string += f"{padding}{' ' * index_ws}{index}{padding}"
        item_name, name_ws = concat_string(string=frame_item.name,
                                           width=20,
                                           padding=0,
                                           trunc_value="...")
        item_string += f"{divider}{padding}{item_name}{' ' * name_ws}{padding}"
        item_type = frame_item.type.capitalize() if frame_item.type != "table_body" else "Table"
        item_type, type_ws = concat_string(string=item_type,
                                           width=6,
                                           padding=0,
                                           trunc_value="")
        item_string += f"{divider}{padding}{item_type}{' ' * type_ws}{padding}"
        item_cols, cols_ws = concat_string(string=len(frame_item.column_list),
                                           width=5,
                                           padding=0,
                                           trunc_value="")
        item_string += f"{divider}{padding}{' ' * cols_ws}{item_cols}{padding}"
        item_rows_list = set_attr_resolver(instance=frame_item, key="row_list", default=[])
        item_rows, rows_ws = concat_string(string=len(item_rows_list),
                                           width=5,
                                           padding=0,
                                           trunc_value="")
        item_rows = item_rows if frame_item.type == "table_body" or frame_item.type == "table_header" else "-"
        item_string += f"{divider}{padding}{' ' * rows_ws}{item_rows}{padding}"
        item_options_list = []
        item_options_list.append("hide_header") if hasattr(frame_item, "hide_header") and frame_item.hide_header is True else None
        item_options_list.append("multiline") if frame_item.frame_styles.multiline is True else None
        item_options_list.append(
            f"max_lines: {frame_item.frame_styles.max_lines}") if frame_item.frame_styles.multiline is True else None
        item_string += f"{divider}{padding}{'; '.join(item_options_list)}{padding}"
        print(item_string)
        frame_index += 1
    print()