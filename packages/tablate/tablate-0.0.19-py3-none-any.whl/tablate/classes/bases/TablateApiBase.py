from copy import copy

from tablate.library.initializers.mappers.element.base.base_column_mapper import base_column_mapper
from tablate.library.initializers.mappers.element.base.base_frame_mapper import base_frame_mapper
from tablate.library.initializers.mappers.element.base.base_text_mapper import base_text_mapper
from tablate.library.initializers.mappers.element.html.html_column_mapper import html_column_mapper
from tablate.library.initializers.mappers.element.html.html_frame_mapper import html_frame_mapper
from tablate.library.initializers.mappers.element.html.html_outer_mapper import html_outer_mapper
from tablate.library.initializers.mappers.element.html.html_text_mapper import html_text_mapper
from tablate.type.type_base import FrameBase
from tablate.type.type_global import HtmlGlobals

from tablate.classes.bases.TablateBase import TablateBase
from tablate.library.renderers.console.render_console import render_console
from tablate.library.renderers.html.render_html import render_html
from tablate.type.defaults import outer_border_default, outer_padding_default, outer_width_default, \
    html_px_multiplier_default, background_padding_default
from tablate.type.primitives import OuterBorder, FrameDivider, OuterWidth, OuterPadding, Background, HtmlPxMultiplier, \
    BackgroundPadding
from tablate.type.type_global import Globals, ConsoleGlobals
from tablate.type.type_input import HtmlOuterStylesInput, ColumnStylesInput, TextStylesInput, \
    HtmlFrameStylesInput, HtmlColumnStylesInput, HtmlTextStylesInput
from tablate.type.type_store import OuterStore


class TablateApiBase(TablateBase):

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

        args = copy(locals())
        del args["self"]

        self._globals = args

        # self._name_list = []

        # default_outer_styles = OuterStore(outer_border=outer_border if outer_border else outer_border_default,
        #                                   outer_padding=outer_padding if outer_padding else outer_padding_default,
        #                                   outer_width=outer_width if outer_width else outer_width_default,
        #                                   background_padding=background_padding if background_padding else background_padding_default)
        #
        # default_frame_styles = base_frame_mapper(frame_input=FrameBase(frame_divider=frame_divider,
        #                                                                background=background))
        #
        # default_column_styles = base_column_mapper(columns_input=column_styles)
        #
        # default_text_styles = base_text_mapper(text_input=text_styles)
        #
        # console_globals = ConsoleGlobals(outer_styles=default_outer_styles,
        #                                  frame_styles=default_frame_styles,
        #                                  column_styles=default_column_styles,
        #                                  text_styles=default_text_styles)
        #
        # if html_px_multiplier is None:
        #     html_px_multiplier = html_px_multiplier_default
        #
        # default_html_outer = html_outer_mapper(html_outer_input=html_styles,
        #                                        base_outer_defaults=default_outer_styles,
        #                                        html_px_multiplier=html_px_multiplier)
        # default_html_frame = html_frame_mapper(html_frame_input=html_frame_styles,
        #                                        base_frame_defaults=default_frame_styles)
        # default_html_column = html_column_mapper(html_columns_input=html_column_styles,
        #                                          base_column_defaults=default_column_styles)
        # default_html_text = html_text_mapper(html_text_input=html_text_styles,
        #                                      base_text_defaults=default_text_styles,
        #                                      html_px_multiplier=html_px_multiplier)
        #
        # html_globals = HtmlGlobals(html_outer_styles=default_html_outer,
        #                            html_frame_styles=default_html_frame,
        #                            html_column_styles=default_html_column,
        #                            html_text_styles=default_html_text,
        #                            css_injection="",
        #                            column_baselines=[],
        #                            styler=None)
        #
        # self._globals: Globals = Globals(console=console_globals, html=html_globals)

        self._frame_list = {}

    # def __is_ipython(self):
    #     return hasattr(__builtins__, "__IPYTHON__")

    # def list_frames(self):
    #     print_frame_list(self._frame_list)

    def to_string(self) -> str:
        return render_console(frame_list=self._frame_list, globals=self._globals)

    def print(self) -> None:
        print(self.to_string())

    def __repr__(self) -> str:
        return self.to_string()

    def to_html(self) -> str:
        return render_html(frame_list=self._frame_list, globals=self._globals)

    def _repr_html_(self) -> str:
        return self.to_html()
