def validate(params):

    if "shape" not in params:

        raise ValueError(
            "Shape missing"
        )

    if not isinstance(params, dict):

        raise ValueError(
            "Invalid parameters"
        )

    return True