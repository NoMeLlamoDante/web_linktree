import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.avatar(color_scheme="indigo", variant="solid", high_contrast=False, fallback="Dante", size="7"),
            rx.text("Edgar Zarate"),
            rx.text("""Hola, Mi nombre es Edgar  pero mis amigos me llaman dante, 
                    soy un desarrollador de software, me gusta la programación y la tecnología
                    en general."""),
            align="center",
            width="50%",
        ),
        width="100%",
        align="center",
    )