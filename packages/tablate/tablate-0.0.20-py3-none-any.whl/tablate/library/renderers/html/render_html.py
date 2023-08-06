from tablate.classes.options.html.style.CssStyler import CssStyler
from tablate.library.calcs.calc_column_percent import calc_column_percent
from tablate.library.initializers.append.append import process_frame_list
from tablate.library.initializers.globals_init import globals_init
from tablate.library.renderers.html.render_html_foot import render_html_foot
from tablate.library.renderers.html.render_html_frames import render_html_frames
from tablate.library.renderers.html.render_html_head import render_html_head
from tablate.type.type_store import FrameStoreList
from tablate.type.type_global import Globals


def render_html(frame_list: dict, globals: dict) -> str:
    globals = globals_init(**globals)
    processed_frame_list = process_frame_list(frame_list=frame_list, globals=globals)

    globals.html.styler = CssStyler()

    globals.html.styler.inject_css_block(globals.html.css_injection)

    return_html = ""

    if len(processed_frame_list) > 0:
        processed_frame_list, column_baselines = calc_column_percent(frame_list=processed_frame_list,
                                                           outer_width=globals.console.outer_styles.outer_width)
        globals.html.column_baselines = column_baselines
        return_html += render_html_head(globals=globals)
        return_html += render_html_frames(frame_list=processed_frame_list, globals=globals)
        return_html += render_html_foot()

    css_head = globals.html.styler.return_head_styles()
    css_foot = globals.html.styler.return_foot_styles()

    return_html = f"{css_head}{return_html}{css_foot}"

    return return_html
