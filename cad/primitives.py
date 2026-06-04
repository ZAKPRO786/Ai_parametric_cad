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
def create_filleted_box(
    length,
    width,
    height,
    fillet_radius
):

    return (
        cq.Workplane("XY")
        .box(length, width, height)
        .edges()
        .fillet(fillet_radius)
    )
def create_chamfered_box(
    length,
    width,
    height,
    chamfer_size
):

    return (
        cq.Workplane("XY")
        .box(length, width, height)
        .edges()
        .chamfer(chamfer_size)
    )
def create_drafted_block():

    return (
        cq.Workplane("XY")
        .rect(50, 50)
        .extrude(
            80,
            taper=5
        )
    )
def create_intersection_demo():

    box = (
        cq.Workplane("XY")
        .box(50, 50, 50)
    )

    cylinder = (
        cq.Workplane("XY")
        .circle(20)
        .extrude(50)
    )

    return box.intersect(cylinder)
def create_housing():

    return (
        cq.Workplane("XY")
        .box(120, 80, 60)
        .faces(">Z")
        .shell(-3)
    )
def create_stepped_shaft():

    section1 = (
        cq.Workplane("YZ")
        .circle(10)
        .extrude(40)
    )

    section2 = (
        cq.Workplane("YZ")
        .workplane(offset=40)
        .circle(15)
        .extrude(40)
    )

    section3 = (
        cq.Workplane("YZ")
        .workplane(offset=80)
        .circle(10)
        .extrude(40)
    )

    return (
        section1
        .union(section2)
        .union(section3)
    )


def create_enclosure_with_standoffs():

    enclosure = (
        cq.Workplane("XY")
        .box(120, 80, 60)
        .faces(">Z")
        .shell(-3)
    )

    positions = [
        (-40, -25),
        (40, -25),
        (-40, 25),
        (40, 25)
    ]

    for x, y in positions:

        boss = (
            cq.Workplane("XY")
            .center(x, y)
            .circle(5)
            .extrude(20)
        )

        enclosure = enclosure.union(
            boss
        )

    return enclosure


def create_clevis_bracket():

    base = (
        cq.Workplane("XY")
        .box(
            120,
            60,
            10
        )
    )

    lug1 = (
        cq.Workplane("XY")
        .center(-15, 0)
        .box(
            20,
            60,
            60
        )
        .translate(
            (0, 0, 30)
        )
    )

    lug2 = (
        cq.Workplane("XY")
        .center(15, 0)
        .box(
            20,
            60,
            60
        )
        .translate(
            (0, 0, 30)
        )
    )

    result = (
        base
        .union(lug1)
        .union(lug2)
    )

    try:

        result = (
            result
            .edges()
            .fillet(3)
        )

    except Exception:

        pass

    return result
def create_advanced_clevis_bracket():

    base = (
        cq.Workplane("XY")
        .box(140, 70, 12)
    )

    lug1 = (
        cq.Workplane("XY")
        .center(-20, 0)
        .box(20, 70, 70)
        .translate((0, 0, 35))
    )

    lug2 = (
        cq.Workplane("XY")
        .center(20, 0)
        .box(20, 70, 70)
        .translate((0, 0, 35))
    )

    result = (
        base
        .union(lug1)
        .union(lug2)
    )

    # Horizontal lug bore
    bore = (
        cq.Workplane("YZ")
        .center(0, 35)
        .circle(8)
        .extrude(100)
    )

    result = result.cut(bore)

    # Mounting holes
    result = (
        result
        .faces(">Z")
        .workplane()
        .pushPoints([
            (-45, -20),
            (45, -20),
            (-45, 20),
            (45, 20)
        ])
        .hole(8)
    )

    # Lightening cutouts
    cut1 = (
        cq.Workplane("YZ")
        .polyline([
            (0, 0),
            (25, 0),
            (0, 25)
        ])
        .close()
        .extrude(80)
    )

    cut2 = (
        cq.Workplane("YZ")
        .polyline([
            (0, 0),
            (-25, 0),
            (0, 25)
        ])
        .close()
        .extrude(80)
    )

    result = result.cut(cut1)
    result = result.cut(cut2)

    try:
        result = result.edges().fillet(3)
    except:
        pass

    return result

def create_engine_cylinder():

    barrel = (
        cq.Workplane("XY")
        .circle(20)
        .extrude(80)
    )

    flange = (
        cq.Workplane("XY")
        .circle(30)
        .circle(20)
        .extrude(8)
    )

    cap = (
        cq.Workplane("XY")
        .workplane(offset=80)
        .circle(25)
        .extrude(8)
    )

    result = (
        barrel
        .union(flange)
        .union(cap)
    )

    for z in range(10, 75, 5):

        fin = (
            cq.Workplane("XY")
            .workplane(offset=z)
            .circle(26)
            .circle(20)
            .extrude(2)
        )

        result = result.union(fin)

    return result

    return result
def create_spiral_staircase():

    result = (
        cq.Workplane("XY")
        .circle(8)
        .extrude(120)
    )

    for i in range(20):

        angle = i * 18
        z = i * 6

        tread = (
            cq.Workplane("XY")
            .center(25, 0)
            .box(
                20,
                8,
                2
            )
            .rotate(
                (0, 0, 0),
                (0, 0, 1),
                angle
            )
            .translate(
                (0, 0, z)
            )
        )

        result = result.union(tread)

    return result


def create_planetary_gear():

    sun = (
        cq.Workplane("XY")
        .circle(10)
        .extrude(10)
    )

    ring = (
        cq.Workplane("XY")
        .circle(60)
        .circle(50)
        .extrude(10)
    )

    result = sun.union(ring)

    for angle in [0, 120, 240]:

        x = 42 * math.cos(
            math.radians(angle)
        )

        y = 42 * math.sin(
            math.radians(angle)
        )

        planet = (
            cq.Workplane("XY")
            .center(x, y)
            .circle(8)
            .extrude(10)
        )

        result = result.union(
            planet
        )

    return result
def create_impeller():

    hub = (
        cq.Workplane("XY")
        .circle(12)
        .extrude(20)
    )

    plate = (
        cq.Workplane("XY")
        .circle(45)
        .circle(12)
        .extrude(3)
    )

    result = hub.union(
        plate
    )

    for angle in range(
        0,
        360,
        30
    ):

        blade = (
            cq.Workplane("XY")
            .center(25, 0)
            .rect(
                20,
                3
            )
            .extrude(15)
            .rotate(
                (0, 0, 0),
                (0, 0, 1),
                angle + 20
            )
        )

        result = result.union(
            blade
        )

    return result
def create_globe_valve():

    # Main body

    body = (
        cq.Workplane("XY")
        .circle(22)
        .extrude(70)
    )

    # Left port

    left_port = (
        cq.Workplane("YZ")
        .center(-35, 0)
        .circle(14)
        .extrude(20)
    )

    # Right port

    right_port = (
        cq.Workplane("YZ")
        .center(35, 0)
        .circle(14)
        .extrude(-20)
    )

    result = (
        body
        .union(left_port)
        .union(right_port)
    )

    # Bonnet

    bonnet = (
        cq.Workplane("XY")
        .workplane(offset=70)
        .circle(14)
        .extrude(20)
    )

    result = result.union(bonnet)

    # Stem

    stem = (
        cq.Workplane("XY")
        .workplane(offset=90)
        .circle(3)
        .extrude(45)
    )

    result = result.union(stem)

    # Handwheel ring

    handwheel = (
        cq.Workplane("XY")
        .workplane(offset=135)
        .circle(25)
        .circle(20)
        .extrude(4)
    )

    result = result.union(handwheel)

    # Hub

    hub = (
        cq.Workplane("XY")
        .workplane(offset=135)
        .circle(5)
        .extrude(8)
    )

    result = result.union(hub)

    # 6 spokes

    for angle in range(0, 360, 60):

        spoke = (
            cq.Workplane("XY")
            .workplane(offset=135)
            .center(12, 0)
            .rect(16, 3)
            .extrude(4)
            .rotate(
                (0, 0, 0),
                (0, 0, 1),
                angle
            )
        )

        result = result.union(spoke)

    try:

        result = (
            result
            .edges("|Z")
            .fillet(2)
        )

    except:

        pass

    return result
def hex_prism(across_flats, height):
    r = across_flats / 2 / math.cos(math.radians(30))
    pts = [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a)))
           for a in range(0, 360, 60)]
    return cq.Workplane("XY").polyline(pts).close().extrude(height)


def create_globe_valve():
    BODY_R = 36
    PIPE_OD = 52
    PIPE_ID = 38
    PORT_LENGTH = 38
    OVERLAP = 10  # ← how far each port penetrates the sphere

    BONNET_HEX_W = 46
    BONNET_FLAT_H = 18
    BONNET_CYL_OD = 32
    BONNET_CYL_H = 22

    STEM_OD = 14
    STEM_LENGTH = 90

    HANDWHEEL_OD = 120
    HANDWHEEL_H = 8
    HUB_OD = 28

    YOKE_H = 30
    YOKE_THICK = 8
    YOKE_W = 50

    NUT_HEX_W = 24
    NUT_H = 14

    # ── 1. SPHERE BODY ────────────────────────────────────────────────────────
    body = cq.Workplane("XY").sphere(BODY_R)

    # ── 2. PORTS  (start INSIDE the sphere so union is connected) ─────────────
    #   Port cylinder total length = OVERLAP (inside) + PORT_LENGTH (outside)
    total_port = PORT_LENGTH + OVERLAP

    # Inlet  (−X)
    inlet = (
        cq.Workplane("XY")
        .transformed(rotate=cq.Vector(0, 90, 0))
        .workplane()
        .circle(PIPE_OD / 2)
        .extrude(total_port)  # extrudes in −X
        .translate((BODY_R - OVERLAP, 0, 0))  # shift so it starts inside
    )
    # mirror to get +X direction properly
    inlet = (
        cq.Workplane("XY")
        .transformed(rotate=cq.Vector(0, -90, 0))
        .workplane()
        .circle(PIPE_OD / 2)
        .extrude(total_port)
        .translate((-BODY_R + OVERLAP, 0, 0))
    )

    # Rebuild both ports cleanly with explicit translation
    def port_cyl(x_center):
        """Cylinder along X-axis centred at x_center."""
        return (
            cq.Workplane("YZ")
            .circle(PIPE_OD / 2)
            .extrude(total_port)  # extrudes in +X from YZ plane
            .translate((x_center, 0, 0))
        )

    # Inlet: extrude from x = -(BODY_R - OVERLAP)  going in −X direction
    inlet = (
        cq.Workplane("YZ")
        .workplane(offset=-(BODY_R - OVERLAP))  # starts inside sphere
        .circle(PIPE_OD / 2)
        .extrude(-total_port)  # negative = −X direction
    )

    # Outlet: extrude from x = +(BODY_R - OVERLAP)  going in +X direction
    outlet = (
        cq.Workplane("YZ")
        .workplane(offset=(BODY_R - OVERLAP))  # starts inside sphere
        .circle(PIPE_OD / 2)
        .extrude(total_port)  # positive = +X direction
    )

    body = body.union(inlet).union(outlet)

    # ── 3. FLOW BORE (through all) ────────────────────────────────────────────
    bore = (
        cq.Workplane("YZ")
        .workplane(offset=-(BODY_R + PORT_LENGTH + 5))
        .circle(PIPE_ID / 2)
        .extrude(2 * (BODY_R + PORT_LENGTH + 5))
    )
    body = body.cut(bore)

    # ── 4. BONNET FLANGE PAD ─────────────────────────────────────────────────
    flange_z = BODY_R - 6
    flange = (
        cq.Workplane("XY")
        .workplane(offset=flange_z)
        .circle(BONNET_HEX_W / 2 + 2)
        .extrude(6)
    )
    body = body.union(flange)

    # ── 5. BONNET HEX ────────────────────────────────────────────────────────
    bonnet_z = flange_z + 6
    bonnet = hex_prism(BONNET_HEX_W, BONNET_FLAT_H).translate((0, 0, bonnet_z))
    body = body.union(bonnet)

    # ── 6. STEM GUIDE (cylindrical) ──────────────────────────────────────────
    guide_z = bonnet_z + BONNET_FLAT_H
    guide = (
        cq.Workplane("XY")
        .workplane(offset=guide_z)
        .circle(BONNET_CYL_OD / 2)
        .extrude(BONNET_CYL_H)
    )
    body = body.union(guide)

    # ── 7. STEM ───────────────────────────────────────────────────────────────
    # Stem starts below the bonnet (inside body) so it's connected
    stem_start_z = BODY_R - 15  # well inside the sphere
    stem_top_z = stem_start_z + STEM_LENGTH + 40
    stem = (
        cq.Workplane("XY")
        .workplane(offset=stem_start_z)
        .circle(STEM_OD / 2)
        .extrude(STEM_LENGTH + 40)
    )
    body = body.union(stem)

    # ── 8. YOKE ARMS (connected to guide, reaching up to handwheel) ──────────
    yoke_base_z = guide_z + BONNET_CYL_H  # top of guide
    yoke_top_z = stem_top_z - 8  # just below handwheel hub bottom

    def yoke_arm(x_sign):
        arm_h = yoke_top_z - yoke_base_z
        return (
            cq.Workplane("XY")
            .workplane(offset=yoke_base_z)
            .rect(YOKE_THICK, YOKE_THICK)
            .extrude(arm_h)
            .translate((x_sign * YOKE_W / 2, 0, 0))
        )

    arm_l = yoke_arm(-1)
    arm_r = yoke_arm(1)

    # Top crosspiece
    arm_h = yoke_top_z - yoke_base_z
    cross = (
        cq.Workplane("XY")
        .workplane(offset=yoke_base_z + arm_h - YOKE_THICK)
        .rect(YOKE_W + YOKE_THICK, YOKE_THICK)
        .extrude(YOKE_THICK)
    )

    body = body.union(arm_l).union(arm_r).union(cross)

    # ── 9. STEM NUT HEX ──────────────────────────────────────────────────────
    nut_z = yoke_top_z
    nut = hex_prism(NUT_HEX_W, NUT_H).translate((0, 0, nut_z))
    body = body.union(nut)

    # ── 10. HANDWHEEL ─────────────────────────────────────────────────────────
    wheel_z = stem_top_z - HANDWHEEL_H  # rim sits at top of stem

    # Hub — extends DOWN to overlap with stem so it's connected
    hub_bottom_z = nut_z  # flush with nut top (they touch)
    hub_top_z = wheel_z + HANDWHEEL_H + 4
    hub_h = hub_top_z - hub_bottom_z

    hub = (
        cq.Workplane("XY")
        .workplane(offset=hub_bottom_z)
        .circle(HUB_OD / 2)
        .extrude(hub_h)
    )
    body = body.union(hub)

    # Rim
    rim = (
        cq.Workplane("XY")
        .workplane(offset=wheel_z)
        .circle(HANDWHEEL_OD / 2)
        .circle(HANDWHEEL_OD / 2 - HANDWHEEL_H)
        .extrude(HANDWHEEL_H)
    )
    body = body.union(rim)

    # Spokes — each goes from hub OD to rim ID, at wheel_z level
    spoke_len = HANDWHEEL_OD / 2 - HANDWHEEL_H - HUB_OD / 2
    spoke_cx = HUB_OD / 2 + spoke_len / 2  # centre X before rotation

    for angle in range(0, 360, 60):
        spoke = (
            cq.Workplane("XY")
            .workplane(offset=wheel_z)
            .transformed(rotate=cq.Vector(0, 0, angle))
            .center(spoke_cx, 0)
            .rect(spoke_len + 2, 6)  # +2 so it overlaps hub & rim
            .extrude(HANDWHEEL_H)
        )
        body = body.union(spoke)

    # ── 11. FILLET (optional, skip if it fails) ───────────────────────────────
    try:
        body = body.edges("|Z").fillet(1.5)
    except Exception:
        pass

    # ── 12. VERIFY ────────────────────────────────────────────────────────────
    combined = body.combine()
    solids = combined.val().Solids()
    print(f"Solid Count: {len(solids)}")
    for i, s in enumerate(solids):
        bb = s.BoundingBox()
        print(f"  Solid {i + 1}: X={bb.xlen:.1f}  Y={bb.ylen:.1f}  Z={bb.zlen:.1f}")

    return combined
def create_tyre_mould():

    OD = 1050
    ID = 520
    HEIGHT = 220

    FLANGE_T = 18

    BOLT_PCD = 1020
    BOLT_D = 22
    N_BOLTS = 24

    # Main ring

    body = (

        cq.Workplane("XY")

        .circle(OD / 2)

        .circle(ID / 2)

        .extrude(HEIGHT)

    )

    # Bottom flange

    bottom_flange = (

        cq.Workplane("XY")

        .workplane(offset=-FLANGE_T)

        .circle((OD + 30) / 2)

        .circle(ID / 2)

        .extrude(FLANGE_T)

    )

    body = body.union(
        bottom_flange
    )

    # Top flange

    top_flange = (

        cq.Workplane("XY")

        .workplane(offset=HEIGHT)

        .circle((OD + 30) / 2)

        .circle(ID / 2)

        .extrude(FLANGE_T)

    )

    body = body.union(
        top_flange
    )

    # Bolt holes

    body = (

        body

        .faces("<Z")

        .workplane()

        .polarArray(
            BOLT_PCD / 2,
            0,
            360,
            N_BOLTS
        )

        .hole(BOLT_D)

    )

    # Alignment bosses

    for angle in range(
        0,
        360,
        90
    ):

        boss = (

            cq.Workplane("XY")

            .workplane(offset=HEIGHT)

            .center(
                (OD / 2 - 50)
                * math.cos(
                    math.radians(angle)
                ),

                (OD / 2 - 50)
                * math.sin(
                    math.radians(angle)
                )
            )

            .circle(25)

            .extrude(30)

        )

        body = body.union(
            boss
        )

    # Tread lugs

    lug_inner = 380
    lug_outer = 408

    for angle in range(
        0,
        360,
        6
    ):

        lug = (

            cq.Workplane("XY")

            .workplane(offset=0)

            .center(
                lug_inner
                * math.cos(
                    math.radians(angle)
                ),

                lug_inner
                * math.sin(
                    math.radians(angle)
                )
            )

            .rect(
                18,
                8
            )

            .extrude(
                HEIGHT * 0.85
            )

            .rotate(
                (0,0,0),
                (0,0,1),
                angle
            )

        )

        body = body.union(
            lug
        )

    try:

        body = (

            body

            .edges("|Z")

            .fillet(2)

        )

    except:

        pass

    body = body.combine()

    print(
        "Solid Count:",
        len(
            body.val().Solids()
        )
    )

    return body