def padding_attr(padding: int, px_multiplier: int = None):
    if px_multiplier is not None:
        padding = padding * px_multiplier
    return f"{padding}px"
