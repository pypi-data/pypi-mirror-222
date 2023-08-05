import vpype as vp
import vpype_cli
import rerun as rr


@vpype_cli.cli.command(group="Plugins")
@vpype_cli.global_processor
def rerun(document: vp.Document) -> vp.Document:
    """Rerun test"""

    rr.init("my data", spawn=True)

    for lid, layer in document.layers.items():
        pen_width = layer.property("vp_pen_width") or document.property("vp_pen_width") or 1.0
        color = layer.property("vp_color") or document.property("vp_color") or vp.Color("blue")

        rr.log_line_strips_2d(
            f"{lid}_layer",
            [vp.as_vector(line) for line in layer],
            timeless=True,
            colors=[color.red, color.green, color.blue],
            stroke_widths=pen_width,
        )

    return document
