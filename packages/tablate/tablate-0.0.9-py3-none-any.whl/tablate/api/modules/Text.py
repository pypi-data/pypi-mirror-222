from typing import Union, Optional

from tablate.classes.bases.TablateApi import TablateApi
from tablate.library.initializers.text_init import text_init
from tablate.type.primitives import TextAlign, FrameDivider, OuterBorder


class Text(TablateApi):

    def __init__(self,
                 # TablateText args
                 text: Union[str, int, float],
                 multiline: bool = True,
                 max_lines: Optional[int] = None,
                 text_align: TextAlign = "left",
                 text_padding: int = 1,
                 frame_divider: FrameDivider = "thick",  # todo: doesn't make sense here
                 trunc_value: str = "...",
                 # TablateApi arge
                 outer_border: OuterBorder = "thick",
                 outer_padding: int = 1,
                 outer_width: int = None,
                 html_px_size: int = 6,
                 html_text_size: int = 12,
                 html_outer_width: str = "100%",
                 html_css_injection: str = "") -> None:

        TablateApi.__init__(self=self,
                            outer_border=outer_border,
                            outer_padding=outer_padding,
                            frame_divider=frame_divider,
                            outer_width=outer_width,
                            html_px_size=html_px_size,
                            html_text_size=html_text_size,
                            html_outer_width=html_outer_width,
                            html_css_injection=html_css_injection)

        text_dict = text_init(text=text,
                              multiline=multiline,
                              max_lines=max_lines,
                              text_align=text_align,
                              text_padding=text_padding,
                              frame_divider=frame_divider,
                              trunc_value=trunc_value,
                              outer_width=self._options["console"]["outer_width"])

        self._frame_list.append(text_dict)