from typing import List

from tablate.classes.bases.TablateApiSet import TablateSet
from tablate.type.primitives import FrameDivider, OuterBorder


def concat(tablate_set: List[TablateUnion],
           outer_border: OuterBorder = "thick",
           outer_padding: int = 1,
           frame_divider: FrameDivider = "thick",
           outer_width: int = None,
           html_px_size: int = 6,
           html_text_size: int = 12,
           html_outer_width: str = "100%",
           html_css_injection: str = ""):

    return TablateSet(tablate_set=tablate_set,
                      outer_border=outer_border,
                      outer_padding=outer_padding,
                      frame_divider=frame_divider,
                      outer_width=outer_width,
                      html_px_size=html_px_size,
                      html_text_size=html_text_size,
                      html_outer_width=html_outer_width,
                      html_css_injection=html_css_injection)