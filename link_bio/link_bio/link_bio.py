""" Principal web """
import reflex as rx
from link_bio.views.header.header import header
from link_bio.views.estudios import estudios
from link_bio.views.experiencia import experiencia
from link_bio.views.footer.footer import footer
from link_bio.styles import styles


def index() -> rx.Component:
    """ Index Web"""
    return rx.flex(
        rx.box(
            # possible navbar ,
            rx.center(
                rx.vstack(
                    header(),
                    # possible link section,
                    experiencia(),
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
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Edgar | Dante Desarrollador de Software",
    description="Página de perfil de Edgar Zarate, desarrollador de software."
)

app._compile()
