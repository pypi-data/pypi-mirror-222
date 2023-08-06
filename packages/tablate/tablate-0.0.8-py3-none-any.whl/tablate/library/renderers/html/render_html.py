from tablate.classes.options.html.style.CssStyler import CssStyler
from tablate.library.calcs.calc_column_percent import calc_column_percent
from tablate.library.renderers.html.render_html_foot import render_html_foot
from tablate.library.renderers.html.render_html_frames import render_html_frames
from tablate.library.renderers.html.render_html_head import render_html_head
from tablate.type.type_store import FrameStoreList
from tablate.type.type_global import Options


def render_html(frame_list: FrameStoreList, options: Options) -> str:

    options.html.styler = CssStyler()

    options.html.styler.inject_css_block(options.html.css_injection)

    return_html = ""

    if len(frame_list) > 0:
        frame_list, column_baselines = calc_column_percent(frame_list=frame_list,
                                                           outer_width=options.console.outer_styles.outer_width)
        options.html.column_baselines = column_baselines
        return_html += render_html_head(options=options)
        return_html += render_html_frames(frame_list=frame_list, options=options)
        return_html += render_html_foot()

    css_head = options.html.styler.return_head_styles()
    css_foot = options.html.styler.return_foot_styles()

    return_html = f"{css_head}{return_html}{css_foot}"

    return return_html
