import reflex as rx
from link_bio.componentes.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links import links
from link_bio.views.estudios import estudios
from link_bio.componentes.footer import footer
import link_bio.styles.styles as styles
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.flex(
        rx.box(
            #navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    #links(),
                    estudios(),
                    max_width="90%",
                    justify="center",
                    align="center", 
                ),
                padding_y=styles.Size.NORMAL_LARGE.value,
            ),
            footer(),
            width="100%",
            justify="center",
            align="center", 
        ),
    )

app = rx.App(
    style = styles.BASE_STYLE,
)
app.add_page(index,
            title="Edgar | Dante Desarrollador de Software",
            description="Página de perfil de Edgar Zarate, desarrollador de software.")
app._compile()