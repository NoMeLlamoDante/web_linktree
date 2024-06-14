import reflex as rx
from link_bio.componentes.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links import links
from link_bio.componentes.footer import footer
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width="600px",
                width="100%",
                margin_y="20px",
                align="center",
            ),
        ),
        footer(),
    )

app = rx.App()
app.add_page(index)
app._compile()