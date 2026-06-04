def plan(prompt: str):

    prompt = prompt.lower()

    if "globe valve" in prompt:
        return "globe_valve"

    if "tyre mould" in prompt:
        return "tyre_mould"

    if "clevis" in prompt:
        return "clevis_bracket"

    if "enclosure" in prompt:
        return "enclosure"

    if "shaft" in prompt:
        return "shaft"

    return "general"