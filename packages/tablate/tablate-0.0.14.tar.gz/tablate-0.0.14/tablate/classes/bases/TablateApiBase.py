from typing import List

from tablate.classes.helpers.list_frame import list_frames
from tablate.library.ascii.chars.line_h import h_line
from tablate.library.ascii.chars.line_v import v_line
from tablate.library.ascii.chars.matrix_cross import cross_matrix
from tablate.library.ascii.chars.matrix_side import left_side_matrix
from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.library.formatters.console.ascii_styler import ascii_text_styler, ascii_terminator
from tablate.library.formatters.console.concat_string import concat_string
from tablate.library.initializers.mappers.element.base.base_column_mapper import base_column_mapper
from tablate.library.initializers.mappers.element.base.base_frame_mapper import base_frame_mapper
from tablate.library.initializers.mappers.element.base.base_text_mapper import base_text_mapper
from tablate.library.initializers.mappers.element.html.html_column_mapper import html_column_mapper
from tablate.library.initializers.mappers.element.html.html_frame_mapper import html_frame_mapper
from tablate.library.initializers.mappers.element.html.html_outer_mapper import html_outer_mapper
from tablate.library.initializers.mappers.element.html.html_text_mapper import html_text_mapper
from tablate.type.type_base import FrameBase, TextBase, ColumnBase
from tablate.type.type_global import HtmlOptions

from tablate.classes.bases.TablateBase import TablateBase
from tablate.library.renderers.console.render_console import render_console
from tablate.library.renderers.html.render_html import render_html
from tablate.type.defaults import outer_border_default, outer_padding_default, outer_width_default, \
    html_px_multiplier_default, background_padding_default
from tablate.type.primitives import OuterBorder, FrameDivider, OuterWidth, OuterPadding, Background, HtmlPxMultiplier, \
    BackgroundPadding
from tablate.type.type_global import Options, ConsoleOptions
from tablate.type.type_input import HtmlOuterStylesInput, ColumnStylesInput, TextStylesInput, \
    HtmlFrameStylesInput, HtmlColumnStylesInput, HtmlTextStylesInput, BaseColumnInput, TableRowsDataInputDict
from tablate.type.type_store import OuterStore, TableHeaderFrameStore, TableBodyFrameStore


class TablateApi(TablateBase):

    def __init__(self,
                 outer_border: OuterBorder = None,
                 outer_padding: OuterPadding = None,
                 outer_width: OuterWidth = None,

                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlOuterStylesInput = None,

                 column_styles: ColumnStylesInput = None,
                 text_styles: TextStylesInput = None,

                 html_frame_styles: HtmlFrameStylesInput = None,

                 html_column_styles: HtmlColumnStylesInput = None,
                 html_text_styles: HtmlTextStylesInput = None) -> None:

        default_outer_styles = OuterStore(outer_border=outer_border if outer_border else outer_border_default,
                                          outer_padding=outer_padding if outer_padding else outer_padding_default,
                                          outer_width=outer_width if outer_width else outer_width_default,
                                          background_padding=background_padding if background_padding else background_padding_default)

        default_frame_styles = base_frame_mapper(frame_input=FrameBase(frame_divider=frame_divider,
                                                                       background=background),
                                                 frame_defaults=FrameBase())

        default_column_styles = base_column_mapper(columns_input=column_styles,
                                                   column_defaults=ColumnBase())

        default_text_styles = base_text_mapper(text_input=text_styles,
                                               text_defaults=TextBase())

        console_options = ConsoleOptions(outer_styles=default_outer_styles,
                                         frame_styles=default_frame_styles,
                                         column_styles=default_column_styles,
                                         text_styles=default_text_styles)

        if html_px_multiplier is None:
            html_px_multiplier = html_px_multiplier_default

        default_html_outer = html_outer_mapper(html_outer_input=html_styles,
                                               base_outer_defaults=default_outer_styles,
                                               html_px_multiplier=html_px_multiplier)
        default_html_frame = html_frame_mapper(html_frame_input=html_frame_styles,
                                               base_frame_defaults=default_frame_styles)
        default_html_column = html_column_mapper(html_columns_input=html_column_styles,
                                                 base_column_defaults=default_column_styles)
        default_html_text = html_text_mapper(html_text_input=html_text_styles,
                                             base_text_defaults=default_text_styles,
                                             html_px_multiplier=html_px_multiplier)

        html_options = HtmlOptions(html_outer_styles=default_html_outer,
                                   html_frame_styles=default_html_frame,
                                   html_column_styles=default_html_column,
                                   html_text_styles=default_html_text,
                                   css_injection="",
                                   column_baselines=[],
                                   styler=None)

        self._options: Options = Options(console=console_options, html=html_options)

        self._frame_list = []

    # def __is_ipython(self):
    #     return hasattr(__builtins__, "__IPYTHON__")

    # def list_frames(self):
    #     print_frame_list(self._frame_list)

    def to_string(self) -> str:
        return render_console(frame_list=self._frame_list, options=self._options)

    def print(self) -> None:
        print(self.to_string())

    def __repr__(self) -> str:
        return self.to_string()

    def to_html(self) -> str:
        return render_html(frame_list=self._frame_list, options=self._options)

    def _repr_html_(self) -> str:
        return self.to_html()
