import reflex as rx
from link_bio.componentes.title import title
from link_bio.styles.styles import Size, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="SB3Ail01.svg",
                variant="solid", 
                high_contrast=False, 
                radius="large",
                fallback="Dante", 
                size="7",
                z_index="-1",
                alt="Logotipo de Edgar Zarate"
            ),
            rx.vstack(
                title("Edgar Zarate"),
                rx.text(
                    "Desarrollador web", 
                    size="2",
                ),
                align="center",
                justify="start",
                spacing="1",
            ),
            justify="center",
            align="center",
        ),
        rx.text(
            """Hola, Mi nombre es Edgar  pero mis amigos me llaman Dante, 
            soy un desarrollador de software, me gusta la programación y la tecnología
            en general.""",
            font_size=Size.MEDIUM.value,
            max_width="60%"
        ),
        align="center",
        justify="center",
        spacing="5"
    )