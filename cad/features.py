import cadquery as cq


def apply_features(
    model,
    features
):

    for feature in features:

        feature_type = feature.get("type")

        # -------------------------
        # Hole Pattern
        # -------------------------

        if feature_type == "hole_pattern":

            try:

                diameter = feature.get(
                    "diameter",
                    8
                )

                spacing_x = feature.get(
                    "spacing_x",
                    80
                )

                spacing_y = feature.get(
                    "spacing_y",
                    40
                )

                model = (
                    model
                    .faces(">Z")
                    .workplane()
                    .rect(
                        spacing_x,
                        spacing_y,
                        forConstruction=True
                    )
                    .vertices()
                    .hole(diameter)
                )

            except Exception:
                pass

        # -------------------------
        # Bolt Circle
        # -------------------------

        elif feature_type == "bolt_circle":

            try:

                count = feature.get(
                    "count",
                    6
                )

                diameter = feature.get(
                    "diameter",
                    6
                )

                pitch_circle = feature.get(
                    "pitch_circle",
                    60
                )

                model = (
                    model
                    .faces(">Z")
                    .workplane()
                    .polarArray(
                        pitch_circle / 2,
                        0,
                        360,
                        count
                    )
                    .hole(diameter)
                )

            except Exception:
                pass

        # -------------------------
        # Chamfer
        # -------------------------

        elif feature_type == "chamfer":

            try:

                size = feature.get(
                    "size",
                    2
                )

                model = (
                    model
                    .faces(">Z")
                    .edges()
                    .chamfer(size)
                )

            except Exception:
                pass

        # -------------------------
        # Fillet
        # -------------------------

        elif feature_type == "fillet":

            try:

                radius = feature.get(
                    "radius",
                    2
                )

                model = (
                    model
                    .edges()
                    .fillet(radius)
                )

            except Exception:
                pass

        # -------------------------
        # Shell
        # -------------------------

        elif feature_type == "shell":

            try:

                thickness = feature.get(
                    "thickness",
                    3
                )

                model = (
                    model
                    .faces(">Z")
                    .shell(-thickness)
                )

            except Exception:
                pass

        # -------------------------
        # Blind Hole
        # -------------------------

        elif feature_type == "blind_hole":

            try:

                diameter = feature.get(
                    "diameter",
                    5
                )

                depth = feature.get(
                    "depth",
                    10
                )

                model = (
                    model
                    .faces(">Z")
                    .workplane()
                    .hole(
                        diameter,
                        depth
                    )
                )

            except Exception:
                pass

        # -------------------------
        # Slot
        # -------------------------

        elif feature_type == "slot":

            try:

                length = feature.get(
                    "length",
                    20
                )

                width = feature.get(
                    "width",
                    8
                )

                model = (
                    model
                    .faces(">Z")
                    .workplane()
                    .slot2D(
                        length,
                        width
                    )
                    .cutBlind(5)
                )

            except Exception:
                pass

        # -------------------------
        # Keyway
        # -------------------------

        elif feature_type == "keyway":

            try:

                width = feature.get(
                    "width",
                    6
                )

                depth = feature.get(
                    "depth",
                    3
                )

                cutter = (
                    cq.Workplane("XY")
                    .box(
                        40,
                        width,
                        depth
                    )
                    .translate(
                        (
                            60,
                            0,
                            15
                        )
                    )
                )

                model = model.cut(
                    cutter
                )

            except Exception:
                pass

        # -------------------------
        # Standoff
        # -------------------------

        elif feature_type == "standoff":

            try:

                diameter = feature.get(
                    "diameter",
                    10
                )

                height = feature.get(
                    "height",
                    20
                )

                positions = feature.get(
                    "positions",
                    [
                        (-40, -25),
                        (40, -25),
                        (-40, 25),
                        (40, 25)
                    ]
                )

                for x, y in positions:

                    boss = (
                        cq.Workplane("XY")
                        .center(x, y)
                        .circle(
                            diameter / 2
                        )
                        .extrude(height)
                    )

                    model = model.union(
                        boss
                    )

            except Exception:
                pass

        # -------------------------
        # Gusset
        # -------------------------

        elif feature_type == "gusset":

            try:

                gusset = (
                    cq.Workplane("YZ")
                    .polyline(
                        [
                            (0, 0),
                            (0, 30),
                            (30, 0)
                        ]
                    )
                    .close()
                    .extrude(5)
                )

                model = model.union(
                    gusset
                )

            except Exception:
                pass

        # -------------------------
        # Rib
        # -------------------------

        elif feature_type == "rib":

            try:

                rib = (
                    cq.Workplane("XY")
                    .box(
                        5,
                        50,
                        30
                    )
                )

                model = model.union(
                    rib
                )

            except Exception:
                pass

    return model