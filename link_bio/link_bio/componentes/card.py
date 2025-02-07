""" Web module: studies card"""
import reflex as rx
from link_bio.styles import styles
from link_bio.componentes.title import subtitle


def card_study(src: any, escuela: str, *cursos: str) -> rx.Component:
    """ Reflex module: card with a image, and a list with each study done"""
    return rx.grid(
        rx.card(
            rx.center(src),
            variant="ghost",
            padding_y=styles.Size.LARGE.value,
        ),
        rx.card(
            rx.vstack(
                subtitle(escuela),
                rx.list.unordered(
                    rx.foreach(
                        cursos,
                        lambda i: rx.list.item(rx.text(i, weight="light")),
                    ),
                ),
                direction="column",
                align="start",
                justify="center",
                height="100%",
                padding_y=styles.Size.LARGE.value,
                padding_x=styles.Size.EXTRA_LARGE.value,
            ),
            variant="ghost",
        ),
        columns=rx.breakpoints(initial="1", sm="2"),
    )
