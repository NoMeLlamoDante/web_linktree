import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles import styles
from link_bio.styles.colors import Color
def navbar() -> rx.Component:
    return rx.hstack(
            rx.heading(
                "Edgar Zarate",
                size = "7",
                weight = "bold",
            ),
            rx.heading(
                "Dante",
                size = "3",
                weight = "medium",
            ),
        justify = "between",
        style=styles.navbar_style,
    )