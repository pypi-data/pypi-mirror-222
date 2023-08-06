from typing import List
from dl_matrix.coordinate import Coordinate
import plotly.graph_objects as go


def animate_conversation_tree(
    coordinates: List[Coordinate], color_scalar: List[int], name: str = "Tree"
):
    hovertext = [
        f"Depth: {coord[0]}<br>Sibling: {coord[3]}<br>Sibling Count: {coord[5]}"
        for coord in coordinates
    ]

    frames = [
        go.Frame(
            data=[
                go.Scatter3d(
                    x=[coord[0] for coord in coordinates[:i]],  # self.depth.x
                    y=[coord[3] for coord in coordinates[:i]],  # self.sibling.y
                    z=[coord[5] for coord in coordinates[:i]],  # self.sibling_count.z
                    mode="markers",
                    marker=dict(
                        size=5,
                        color=color_scalar[:i],
                        colorscale="rainbow",
                        colorbar=dict(
                            title="Labels",
                            x=-0.1,
                            xanchor="left",
                        ),
                        line=dict(color="powderblue", width=2),
                        opacity=0.9,
                        symbol="circle",
                        sizemode="diameter",
                    ),
                    hoverinfo="text",
                    hovertext=hovertext,
                    name="Coordinates",
                ),
                go.Scatter3d(
                    x=[coord[0] for coord in coordinates[:i]],  # self.depth.x
                    y=[coord[3] for coord in coordinates[:i]],  # self.sibling.y
                    z=[coord[5] for coord in coordinates[:i]],  # self.sibling_count.z
                    mode="lines",
                    line=dict(color="white", width=1),
                    hoverinfo="none",
                ),
            ]
        )
        for i in range(1, len(coordinates) + 1)
    ]

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=[coord[0] for coord in coordinates],  # self.depth.x
                y=[coord[3] for coord in coordinates],  # self.sibling.y
                z=[coord[5] for coord in coordinates],  # self.sibling_count.z
                mode="markers",
                marker=dict(
                    size=5,
                    color=color_scalar,
                    colorscale="rainbow",
                    colorbar=dict(
                        title="Labels",
                        x=-0.1,
                        xanchor="left",
                    ),
                    line=dict(color="powderblue", width=2),
                    opacity=0.9,
                    symbol="circle",
                    sizemode="diameter",
                ),
                hoverinfo="text",
                name="Coordinates",
            ),
            go.Scatter3d(
                x=[coord[0] for coord in coordinates],  # self.depth.x
                y=[coord[3] for coord in coordinates],  # self.sibling.y
                z=[coord[5] for coord in coordinates],  # self.sibling_count.z
                mode="lines",
                line=dict(color="white", width=1),
                hoverinfo="none",
            ),
        ],
        layout=go.Layout(
            title=name,
            scene=dict(
                xaxis=dict(showbackground=False, gridcolor="Black"),
                yaxis=dict(showbackground=False, gridcolor="Black"),
                zaxis=dict(showbackground=False, gridcolor="Black"),
                camera=dict(
                    up=dict(x=0, y=0, z=1),
                    eye=dict(x=-1.5, y=-1.5, z=1.5),
                    center=dict(x=0, y=0, z=0),
                ),
                dragmode="turntable",
            ),
            font_family="Arial",
            font_color="White",
            title_font_family="Arial",
            title_font_color="White",
            legend_title_font_color="White",
            paper_bgcolor="Black",
            plot_bgcolor="Black",
            hoverlabel=dict(bgcolor="Black", font_color="White"),
            updatemenus=[
                dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(
                            label="Play",
                            method="animate",
                            args=[
                                None,
                                dict(frame=dict(duration=500, redraw=True)),
                            ],
                        )
                    ],
                )
            ],
        ),
        frames=frames,
    )
    fig.show()
