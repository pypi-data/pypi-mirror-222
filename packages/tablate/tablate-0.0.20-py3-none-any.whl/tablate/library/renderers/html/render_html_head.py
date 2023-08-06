from tablate.library.formatters.html.style.attributes.divider import divider_attr
from tablate.library.formatters.html.style.attributes.margin import margin_attr
from tablate.library.formatters.html.style.attributes.padding import padding_attr
from tablate.library.formatters.html.style.attributes.space import space_attr
from tablate.type.type_global import Globals


def render_html_head(globals: Globals) -> str:

    outer_padding = globals.html.html_outer_styles.html_outer_padding
    frame_border_style = globals.html.html_outer_styles.html_outer_border_style
    frame_border_weight = globals.html.html_outer_styles.html_outer_border_weight
    html_px_multiplier = globals.html.html_outer_styles.html_px_multiplier

    html_width = globals.html.html_outer_styles.html_outer_width
    column_baselines = globals.html.column_baselines

    margin_left_px = outer_padding
    margin_string = f'0 {margin_left_px}px'

    border_string = divider_attr(divider_style=frame_border_style, divider_weight=frame_border_weight)

    globals.html.styler.add_global_style_attribute("font-family", "'Roboto', sans-serif")
    globals.html.styler.add_global_style_attribute("box-sizing", "border-box")
    globals.html.styler.add_global_style_attribute("margin", 0)
    globals.html.styler.add_global_style_attribute("padding", 0)

    margin_edge = space_attr(html_spacer=margin_left_px, html_px_multiplier=html_px_multiplier)[1]

    globals.html.styler.wrapper.add_style_attribute("width", f"calc({html_width}-{margin_edge}px)")
    globals.html.styler.wrapper.add_style_attribute("margin", margin_attr(margin=margin_left_px,
                                                                          html_px_multiplier=html_px_multiplier))

    globals.html.styler.table.add_style_attribute("width", "100%")
    globals.html.styler.table.add_style_attribute("border", border_string)

    globals.html.styler.table.add_style_attribute("border-collapse", "collapse")

    wrapper_classes = globals.html.styler.wrapper.generate_class_names()
    table_classes = globals.html.styler.table.generate_class_names()

    return_string = ''

    return_string += f'<div class="{wrapper_classes}">'
    return_string += f'<table class="{table_classes}">'

    return_string += f'<colgroup>'

    previous_baseline_value = 0
    for baseline_column_width in column_baselines:
        column_width = baseline_column_width - previous_baseline_value
        return_string += f'<col style="width:{column_width}%;">'
        previous_baseline_value = baseline_column_width
    return_string += f'</colgroup>'

    return return_string

