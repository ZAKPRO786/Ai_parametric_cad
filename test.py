from ocp_vscode import show
import cadquery as cq

part = (
    cq.Workplane("XY")
    .box(100, 50, 20)
)

show(part)