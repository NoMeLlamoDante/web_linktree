import reflex as rx
from link_bio.componentes.navbar import navbar

class State(rx.State):
    pass


def index() -> rx.Component:
    return navbar()

app = rx.App()
app.add_page(index)
app._compile()