from parser.extractor import extract_number


def parse_prompt(prompt: str):

    prompt = prompt.lower()

    if "cylinder" in prompt:

        radius = extract_number(
            r"radius\s*(\d+)",
            prompt
        )

        height = extract_number(
            r"height\s*(\d+)",
            prompt
        )

        return {
            "shape": "cylinder",
            "radius": radius,
            "height": height
        }

    elif "box" in prompt:

        length = extract_number(
            r"length\s*(\d+)",
            prompt
        )

        width = extract_number(
            r"width\s*(\d+)",
            prompt
        )

        height = extract_number(
            r"height\s*(\d+)",
            prompt
        )

        return {
            "shape": "box",
            "length": length,
            "width": width,
            "height": height
        }

    elif "spacer" in prompt:

        outer_radius = extract_number(
            r"outer\s*(\d+)",
            prompt
        )

        inner_radius = extract_number(
            r"inner\s*(\d+)",
            prompt
        )

        height = extract_number(
            r"height\s*(\d+)",
            prompt
        )

        return {
            "shape": "spacer",
            "outer_radius": outer_radius,
            "inner_radius": inner_radius,
            "height": height
        }

    raise ValueError("Unsupported shape")