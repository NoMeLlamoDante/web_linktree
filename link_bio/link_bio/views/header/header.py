import reflex as rx
from link_bio.componentes.title import title
from link_bio.styles.styles import Size, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                color_scheme="jade",
                variant="solid", 
                high_contrast=False, 
                radius="large",
                fallback="Dante", 
                size="7",
                z_index="-1",
            ),
            rx.vstack(
                title("Edgar Zarate"),
                rx.text(
                    "Desarrollador de software", 
                    size="2",
                ),
                align="center",
                justify="start",
                spacing="0",
            ),
            justify="center",
            align="center",
        ),
        rx.text(
            """Hola, Mi nombre es Edgar  pero mis amigos me llaman dante, 
            soy un desarrollador de software, me gusta la programación y la tecnología
            en general.""",
            max_width="60%"
        ),
        align="center",
        justify="center",
        spacing="5"
    )