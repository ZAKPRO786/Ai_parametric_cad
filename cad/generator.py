from cad.primitives import *
from cad.features import apply_features


def generate_model(params):

    shape = params["shape"]

    model = None

    if shape == "cylinder":

        model = create_cylinder(
            params["radius"],
            params["height"]
        )

    elif shape == "box":

        model = create_box(
            params["length"],
            params["width"],
            params["height"]
        )

    elif shape == "spacer":

        model = create_spacer(
            params["outer_radius"],
            params["inner_radius"],
            params["height"]
        )

    elif shape == "pipe":

        model = create_pipe(
            params["outer_radius"],
            params["inner_radius"],
            params["height"]
        )

    elif shape == "plate":

        model = create_plate(
            params["length"],
            params["width"],
            params["thickness"]
        )

    elif shape == "bracket":

        model = create_bracket(
            params["length"],
            params["width"],
            params["height"],
            params["thickness"]
        )

    elif shape == "gear":

        model = create_gear(
            params["teeth"],
            params["module"],
            params["thickness"],
            params["bore_radius"]
        )

    elif shape == "pulley":

        model = create_pulley(
            params["outer_diameter"],
            params["bore_diameter"],
            params["width"]
        )

    elif shape == "shaft":

        model = create_shaft(
            params["diameter"],
            params["length"]
        )

    elif shape == "stepped_shaft":

        model = create_stepped_shaft()

    elif shape == "flange":

        model = create_flange(
            params["outer_diameter"],
            params["thickness"],
            params["bore_diameter"]
        )

    elif shape == "cone":

        model = create_cone(
            params["radius"],
            params["height"]
        )

    elif shape == "mounting_plate":

        model = create_mounting_plate(
            params["length"],
            params["width"],
            params["thickness"],
            params["hole_diameter"]
        )

    elif shape == "filleted_box":

        model = create_filleted_box(
            params["length"],
            params["width"],
            params["height"],
            params["fillet_radius"]
        )

    elif shape == "chamfered_box":

        model = create_chamfered_box(
            params["length"],
            params["width"],
            params["height"],
            params["chamfer_size"]
        )

    elif shape == "drafted_block":

        model = create_drafted_block()

    elif shape == "intersection_demo":

        model = create_intersection_demo()

    elif shape == "housing":

        model = create_housing()

    elif shape == "enclosure":

        model = create_enclosure_with_standoffs()

    elif shape == "clevis_bracket":

        model = create_clevis_bracket()
    elif shape == "advanced_clevis_bracket":

        model = create_advanced_clevis_bracket()

    elif shape == "engine_cylinder":

        model = create_engine_cylinder()

    elif shape == "planetary_gear":

        model = create_planetary_gear()

    elif shape == "spiral_staircase":

        model = create_spiral_staircase()

    elif shape == "impeller":

        model = create_impeller()
    elif shape == "globe_valve":

        model = create_globe_valve()
    elif shape == "tyre_mould":

        model = create_tyre_mould()
    else:

        raise ValueError(
            f"Unsupported shape: {shape}"
        )

    # -------------------------
    # Apply Features
    # -------------------------

    features = params.get(
        "features",
        []
    )

    if features:

        model = apply_features(
            model,
            features
        )

    return model