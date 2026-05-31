import cadquery as cq


def execute_custom_code(code):

    safe_globals = {
        "cq": cq
    }
    FORBIDDEN = [
        ".cutAll(",
        ".cutCircle(",
        ".gear(",
        ".cone(",
        ".pulley(",
        ".flange("
    ]

    for api in FORBIDDEN:
        if api in code:
            raise ValueError(
                f"Unsupported CadQuery API detected: {api}"
            )
    exec(code, safe_globals)

    if "result" not in safe_globals:
        raise ValueError(
            "Generated code must create a variable named 'result'"
        )

    return safe_globals["result"]