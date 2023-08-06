from tablate.type.primitives import FrameNameList
from tablate.type.type_store import FrameStoreList
from tablate.type.type_global import Options


class TablateBase:

    _options: Options

    _frame_list: FrameStoreList

    _name_list: FrameNameList
