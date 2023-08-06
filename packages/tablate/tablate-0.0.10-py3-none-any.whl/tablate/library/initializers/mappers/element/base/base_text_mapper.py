from typing import Optional

from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.type.defaults import text_style_default, text_align_default, text_color_default
from tablate.type.type_base import TextBase
from tablate.type.type_store import TextStore


def base_text_mapper(text_input: Optional[TextBase] = None,
                     text_defaults: Optional[TextBase] = None) -> TextStore:
    if text_input is None:
        text_input = TextBase()

    text_return = TextStore(text_style=set_attr_resolver(instance=text_input,
                                                         key="text_style",
                                                         default=set_attr_resolver(instance=text_defaults,
                                                                                   key="text_style",
                                                                                   default=text_style_default)),
                            text_align=set_attr_resolver(instance=text_input,
                                                         key="text_align",
                                                         default=set_attr_resolver(instance=text_defaults,
                                                                                   key="text_align",
                                                                                   default=text_align_default)),
                            text_color=set_attr_resolver(instance=text_input,
                                                         key="text_color",
                                                         default=set_attr_resolver(instance=text_defaults,
                                                                                   key="text_color",
                                                                                   default=text_color_default)))

    return text_return
