import reflex as rx
from link_bio.componentes.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links import links
from link_bio.componentes.footer import footer
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )

app = rx.App()
app.add_page(index)
app._compile()