from typing import Optional

from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.type.defaults import background_default, max_lines_default, \
    multiline_default, trunc_value_default, frame_divider_default, background_padding_default, table_multiline_default
from tablate.type.type_base import FrameBase
from tablate.type.type_store import FrameStore


def base_frame_mapper(frame_input: Optional[FrameBase] = None,
                      frame_defaults: Optional[FrameBase] = None) -> FrameStore:
    frame_return = FrameStore(frame_divider=set_attr_resolver(instance=frame_input,
                                                              key="frame_divider",
                                                              default=set_attr_resolver(instance=frame_defaults,
                                                                                        key="frame_divider",
                                                                                        default=frame_divider_default)),
                              max_lines=set_attr_resolver(instance=frame_input,
                                                          key="max_lines",
                                                          default=set_attr_resolver(instance=frame_defaults,
                                                                                    key="max_lines",
                                                                                    default=max_lines_default)),
                              multiline=set_attr_resolver(instance=frame_input,
                                                          key="multiline",
                                                          default=set_attr_resolver(instance=frame_defaults,
                                                                                    key="multiline",
                                                                                    default=multiline_default)),
                              background=set_attr_resolver(instance=frame_input,
                                                           key="background",
                                                           default=set_attr_resolver(instance=frame_defaults,
                                                                                     key="background",
                                                                                     default=background_default)),
                              trunc_value=set_attr_resolver(instance=frame_input,
                                                            key="trunc_value",
                                                            default=set_attr_resolver(instance=frame_defaults,
                                                                                      key="trunc_value",
                                                                                      default=trunc_value_default)))

    return frame_return
