""" Web module: button """
import reflex as rx
from link_bio.styles import styles


def link_button(label: str, url: str, icon: str = None) -> rx.Component:
    """ Reflex module: Button with an icon labeled """
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(icon if icon else "external-link"),
                rx.text(
                    label, 
                    style=styles.button_tittle_style
                ), 
                widht="100%",
                align="center",
                alt=label,
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )


def icon_button(url: str, icon: str = None) -> rx.Component:
    """ Reflex module: Button with an icon """
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(icon if icon else "external-link"),
                widht="100%",
                align="center",
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )
