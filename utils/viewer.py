import plotly.graph_objects as go


def cadquery_to_plotly(workplane):

    shape = workplane.val()

    vertices, triangles = shape.tessellate(0.5)

    x = [v.x for v in vertices]
    y = [v.y for v in vertices]
    z = [v.z for v in vertices]

    i = [t[0] for t in triangles]
    j = [t[1] for t in triangles]
    k = [t[2] for t in triangles]

    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=x,
                y=y,
                z=z,
                i=i,
                j=j,
                k=k,
                opacity=1.0
            )
        ]
    )

    fig.update_layout(
        scene_aspectmode="data",
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )

    return fig