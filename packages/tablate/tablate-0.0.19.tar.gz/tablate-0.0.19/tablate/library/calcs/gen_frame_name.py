def gen_frame_name(name: str, type: str, frame_dict: dict):
    if name is not None:
        return name
    else:
        untitled_frame_name = f"Untited{type.capitalize()}Frame0"
        for frame_index, (frame_key, _) in enumerate(frame_dict.items()):
            untitled_frame_name = f"Untited{type.capitalize()}Frame{frame_index}"
            if untitled_frame_name in frame_dict:
                continue
            else:
                return untitled_frame_name
        return untitled_frame_name