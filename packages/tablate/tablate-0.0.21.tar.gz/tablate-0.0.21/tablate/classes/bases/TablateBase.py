from typing import List

from tablate.type.primitives import FrameNameList
from tablate.type.type_store import FrameStoreList
from tablate.type.type_global import Globals


class TablateBase:

    _globals: dict

    _frame_list: dict

    _name_list: FrameNameList
