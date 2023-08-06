from tablate.library.formatters.html.style.attributes.divider import divider_attr
from tablate.type.type_global import Options


def render_html_head(options: Options) -> str:

    outer_padding = options.html.html_outer_styles.html_outer_padding
    frame_border_style = options.html.html_outer_styles.html_outer_border_style
    frame_border_weight = options.html.html_outer_styles.html_outer_border_weight

    html_width = options.html.html_outer_styles.html_outer_width
    column_baselines = options.html.column_baselines

    margin_left_px = outer_padding
    margin_string = f'0 {margin_left_px}px'

    border_string = divider_attr(divider_style=frame_border_style, divider_weight=frame_border_weight)

    options.html.styler.add_global_style_attribute("font-family", "'Roboto', sans-serif")
    options.html.styler.add_global_style_attribute("box-sizing", "border-box")
    options.html.styler.add_global_style_attribute("margin", 0)
    options.html.styler.add_global_style_attribute("padding", 0)

    options.html.styler.wrapper.add_style_attribute("width", f"calc({html_width} - {margin_left_px * 2}px)")
    options.html.styler.wrapper.add_style_attribute("margin", margin_string)

    options.html.styler.table.add_style_attribute("width", "100%")
    options.html.styler.table.add_style_attribute("border", border_string)

    options.html.styler.table.add_style_attribute("border-collapse", "collapse")

    wrapper_classes = options.html.styler.wrapper.generate_class_names()
    table_classes = options.html.styler.table.generate_class_names()

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

