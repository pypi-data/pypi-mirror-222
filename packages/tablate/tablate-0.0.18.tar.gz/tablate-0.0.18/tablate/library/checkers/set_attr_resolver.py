from dataclasses import dataclass
from typing import Any, Type


def set_attr_resolver(instance: Any, key: str, default: Any):
    return instance.__getattribute__(key) if hasattr(instance, key) and instance.__getattribute__(key) is not None else default

