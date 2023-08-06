from typing import Optional

from tablate.library.initializers.mappers.element.base.base_column_mapper import base_column_mapper
from tablate.library.initializers.mappers.element.base.base_frame_mapper import base_frame_mapper
from tablate.library.initializers.mappers.element.base.base_text_mapper import base_text_mapper
from tablate.library.initializers.mappers.element.html.html_column_mapper import html_column_mapper
from tablate.library.initializers.mappers.element.html.html_frame_mapper import html_frame_mapper
from tablate.library.initializers.mappers.element.html.html_text_mapper import html_text_mapper
from tablate.type.defaults import html_px_multiplier_default
from tablate.type.primitives import HtmlPxMultiplier
from tablate.type.type_base import FrameBase, TextBase, ColumnBase
from tablate.type.type_global import Options
from tablate.type.type_input import BaseStylesInput, HtmlStylesInput
from tablate.type.type_store import BaseFrameStore


def style_mapper(base_input: Optional[BaseStylesInput],
                 html_input: Optional[HtmlStylesInput],
                 frame_default: Optional[FrameBase],
                 column_default: Optional[ColumnBase],
                 text_default: Optional[TextBase],
                 html_px_multiplier: HtmlPxMultiplier,
                 options: Options) -> BaseFrameStore:

    if html_px_multiplier is None:
        html_px_multiplier = html_px_multiplier_default

    frame_styles = base_frame_mapper(frame_input=options.console.frame_styles)
    column_styles = base_column_mapper(columns_input=options.console.column_styles)
    text_styles = base_text_mapper(text_input=options.console.text_styles)

    if frame_default:
        frame_styles = base_frame_mapper(frame_input=frame_default, frame_defaults=frame_styles)
    if column_default:
        column_styles = base_column_mapper(columns_input=column_default, column_defaults=column_styles)
    if text_default:
        text_styles = base_text_mapper(text_input=text_default, text_defaults=text_styles)

    if base_input:
        if base_input.frame_styles:
            frame_styles = base_frame_mapper(frame_input=base_input.frame_styles, frame_defaults=frame_styles)
        if base_input.column_styles:
            column_styles = base_column_mapper(columns_input=base_input.column_styles, column_defaults=column_styles)
        if base_input.text_styles:
            text_styles = base_text_mapper(text_input=base_input.text_styles, text_defaults=text_styles)

    html_frame_styles = html_frame_mapper(base_frame_defaults=frame_styles, html_px_multiplier=html_px_multiplier)
    html_column_styles = html_column_mapper(base_column_defaults=column_styles)
    html_text_styles = html_text_mapper(base_text_defaults=text_styles)


    if html_input:
        if html_input.html_frame_styles:
            html_frame_styles = html_frame_mapper(html_frame_input=html_input.html_frame_styles,
                                                  base_frame_defaults=frame_styles)
        if html_input.html_column_styles:
            html_column_styles = html_column_mapper(html_columns_input=html_input.html_column_styles,
                                                    base_column_defaults=column_styles)
        if html_input.html_text_styles:
            html_text_styles = html_text_mapper(html_text_input=html_input.html_text_styles,
                                                base_text_defaults=text_styles,
                                                html_px_multiplier=html_px_multiplier)

    return BaseFrameStore(frame_styles=frame_styles,
                          column_styles=column_styles,
                          text_styles=text_styles,
                          html_frame_styles=html_frame_styles,
                          html_column_styles=html_column_styles,
                          html_text_styles=html_text_styles)
