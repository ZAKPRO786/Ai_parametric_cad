import cadquery as cq

import math
def create_cylinder(radius, height):

    return (
        cq.Workplane("XY")
        .circle(radius)
        .extrude(height)
    )


def create_box(length, width, height):

    return (
        cq.Workplane("XY")
        .box(length, width, height)
    )


def create_spacer(
    outer_radius,
    inner_radius,
    height
):

    outer = (
        cq.Workplane("XY")
        .circle(outer_radius)
        .extrude(height)
    )

    inner = (
        cq.Workplane("XY")
        .circle(inner_radius)
        .extrude(height)
    )

    return outer.cut(inner)
def create_pipe(
    outer_radius,
    inner_radius,
    height
):

    return (
        cq.Workplane("XY")
        .circle(outer_radius)
        .circle(inner_radius)
        .extrude(height)
    )
def create_plate(
    length,
    width,
    thickness
):

    return (
        cq.Workplane("XY")
        .box(
            length,
            width,
            thickness
        )
    )
def create_bracket(
    length,
    width,
    height,
    thickness
):

    base = (
        cq.Workplane("XY")
        .box(
            length,
            width,
            thickness
        )
    )

    wall = (
        cq.Workplane("YZ")
        .box(
            thickness,
            width,
            height
        )
    )

    return base.union(wall)
def create_gear(
    teeth,
    module,
    thickness,
    bore_radius
):

    pitch_radius = teeth * module / 2

    gear = (
        cq.Workplane("XY")
        .circle(pitch_radius)
        .circle(bore_radius)
        .extrude(thickness)
    )

    tooth_width = module
    tooth_height = module

    for i in range(teeth):

        angle = (360 / teeth) * i

        tooth = (
            cq.Workplane("XY")
            .center(
                pitch_radius,
                0
            )
            .rect(
                tooth_width,
                tooth_height
            )
            .extrude(thickness)
            .rotate(
                (0, 0, 0),
                (0, 0, 1),
                angle
            )
        )

        gear = gear.union(tooth)

    return gear
def create_pulley(
    outer_diameter,
    bore_diameter,
    width
):

    outer_radius = outer_diameter / 2
    bore_radius = bore_diameter / 2

    result = (
        cq.Workplane("XY")
        .circle(outer_radius)
        .circle(bore_radius)
        .extrude(width)
    )

    result = (
        result
        .edges("|Z")
        .fillet(2)
    )

    return result
def create_shaft(
    diameter,
    length
):

    return (
        cq.Workplane("XY")
        .circle(diameter / 2)
        .extrude(length)
        .edges("|Z")
        .chamfer(1)
    )
def create_flange(
    outer_diameter,
    thickness,
    bore_diameter
):

    result = (
        cq.Workplane("XY")
        .circle(outer_diameter / 2)
        .circle(bore_diameter / 2)
        .extrude(thickness)
    )

    result = (
        result
        .faces(">Z")
        .workplane()
        .polarArray(
            outer_diameter * 0.35,
            0,
            360,
            6
        )
        .hole(8)
    )

    return result
def create_valve_stem():

    profile = (
        cq.Workplane("XZ")
        .moveTo(5, 0)
        .lineTo(5, 100)
        .lineTo(0, 100)
        .close()
    )

    return profile.revolve()

def create_cone(radius, height):

    return (
        cq.Workplane("XZ")
        .moveTo(0, 0)
        .lineTo(radius, 0)
        .lineTo(0, height)
        .close()
        .revolve()
    )
def create_mounting_plate(
    length,
    width,
    thickness,
    hole_diameter
):

    hole_offset_x = length / 2 - 10
    hole_offset_y = width / 2 - 10

    return (
        cq.Workplane("XY")
        .box(length, width, thickness)
        .faces(">Z")
        .workplane()
        .pushPoints([
            (-hole_offset_x, -hole_offset_y),
            ( hole_offset_x, -hole_offset_y),
            (-hole_offset_x,  hole_offset_y),
            ( hole_offset_x,  hole_offset_y)
        ])
        .hole(hole_diameter)
    )