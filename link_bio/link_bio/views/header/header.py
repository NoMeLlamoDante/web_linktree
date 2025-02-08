""" Web section: Header """
import reflex as rx
from link_bio.componentes.title import principal
from link_bio.styles.styles import Size
from link_bio.data import text
from link_bio.componentes.link_button import icon_button
from link_bio.data import constants


def header() -> rx.Component:
    """ Reflex module: Header """
    return rx.section(
        rx.flex(
            rx.stack(
                rx.stack(
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
                    width=rx.breakpoints(initial="100%", sm="30%"),
                    align="center",
                    justify="center",
                ),
                rx.vstack(
                    principal(text.NAME),
                    rx.text(text.JOB, size="4"),
                    # Ubicación
                    rx.card(
                        rx.hstack(
                                rx.icon("map-pin"),
                                rx.text(text.CITY, weight="light"),
                        ),
                        variant="ghost"
                    ),
                    # links
                    rx.hstack(
                        icon_button(constants.GITHUB_URL, "github"),
                        icon_button(constants.LINKEDIN_URL, "linkedin"),
                    ),
                    flex_direction="column",
                    width="100%",
                ),
                width="100%",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                align="center",
                justify="center",
            ),
            width="100%",
            align="center",
            justify="center",
        ),
        rx.vstack(
            rx.text(
                text.COMPLETE_BIO,
                font_size="3",
                padding_y=rx.breakpoints(
                    initial=Size.NORMAL.value,
                    sm=Size.NORMAL_LARGE.value),
            ),
        ),
        width=rx.breakpoints(initial="90%", sm="60%"),
        align="center",
        justify="center",
    )
