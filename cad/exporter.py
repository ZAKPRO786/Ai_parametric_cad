import cadquery as cq


def export_stl(
    model,
    filename="outputs/output.stl"
):

    cq.exporters.export(
        model,
        filename
    )

    return filename