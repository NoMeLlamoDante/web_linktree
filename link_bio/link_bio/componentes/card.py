import reflex as rx
import link_bio.styles.styles as styles
from link_bio.componentes.title import subtitle

def card_study(src: any , escuela: str, *cursos: str ) -> rx.Component:
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
                    align=rx.breakpoints(initial="center", sm="start"),
                    justify="center",
                    height="100%",
                    padding_y=styles.Size.LARGE.value,
                    padding_x=styles.Size.EXTRA_LARGE.value,
                ),
                variant="ghost",
            ),
            columns=rx.breakpoints(initial="1", sm="2"),
        ),