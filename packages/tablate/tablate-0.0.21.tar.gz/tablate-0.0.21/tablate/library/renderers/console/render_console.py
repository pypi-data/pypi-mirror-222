from tablate.library.initializers.append.append import process_frame_list
from tablate.library.initializers.globals_init import globals_init
from tablate.library.initializers.text_init import text_init
from tablate.library.initializers.grid_init import grid_init
from tablate.library.initializers.table_init import table_init
from tablate.library.renderers.console.render_console_foot import render_console_foot
from tablate.library.renderers.console.render_console_frames import render_console_frames
from tablate.library.renderers.console.render_console_head import render_console_head
from tablate.type.type_store import FrameStoreList
from tablate.type.type_global import Globals


def render_console(frame_list: dict, globals: dict) -> str:
    globals = globals_init(**globals)
    processed_frame_list = process_frame_list(frame_list=frame_list, globals=globals)
    return_string = ""
    if len(processed_frame_list) > 0:
        return_string += render_console_head(frame_list=processed_frame_list, globals=globals)
        return_string += render_console_frames(frame_list=processed_frame_list, globals=globals)
        return_string += render_console_foot(frame_list=processed_frame_list, globals=globals)
    return return_string
