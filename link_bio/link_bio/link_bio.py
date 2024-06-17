import reflex as rx
from link_bio.componentes.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links import links
from link_bio.componentes.footer import footer
import link_bio.styles.styles as styles
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                margin_y=styles.Size.LARGE.value,
                align="center",
            ),
            width="100%",
        ),
        footer(),
    )

app = rx.App(
    style = styles.BASE_STYLE,
)
app.add_page(index)
app._compile()