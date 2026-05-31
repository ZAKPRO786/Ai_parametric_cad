from cad.custom_executor import execute_custom_code
from cad.primitives import *

def generate_model(params):

    shape = params["shape"]

    if shape == "cylinder":

        return create_cylinder(
            params["radius"],
            params["height"]
        )

    elif shape == "box":

        return create_box(
            params["length"],
            params["width"],
            params["height"]
        )

    elif shape == "spacer":

        return create_spacer(
            params["outer_radius"],
            params["inner_radius"],
            params["height"]
        )

    elif shape == "pipe":

        return create_pipe(
            params["outer_radius"],
            params["inner_radius"],
            params["height"]
        )

    elif shape == "plate":

        return create_plate(
            params["length"],
            params["width"],
            params["thickness"]
        )

    elif shape == "bracket":

        return create_bracket(
            params["length"],
            params["width"],
            params["height"],
            params["thickness"]
        )

    elif shape == "gear":

        return create_gear(
            params["teeth"],
            params["module"],
            params["thickness"],
            params["bore_radius"]
        )
    elif shape == "custom":

        return execute_custom_code(
            params["cadquery_code"]
        )
    elif shape == "pulley":

        return create_pulley(
            params["outer_diameter"],
            params["bore_diameter"],
            params["width"]
        )

    elif shape == "shaft":

        return create_shaft(
            params["diameter"],
            params["length"]
        )

    elif shape == "flange":

        return create_flange(
            params["outer_diameter"],
            params["thickness"],
            params["bore_diameter"]
        )
    elif shape == "cone":

        return create_cone(
            params["radius"],
            params["height"]
        )
    elif shape == "mounting_plate":

        return create_mounting_plate(
            params["length"],
            params["width"],
            params["thickness"],
            params["hole_diameter"]
        )
    raise ValueError(f"Unsupported shape: {shape}")