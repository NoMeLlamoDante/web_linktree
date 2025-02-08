""" Navbar Items """
import reflex as rx
from link_bio.styles import styles


def navbar_logo() -> rx.Component:
    """ Navbar component: Navbar with logo """
    return rx.hstack(
        rx.image(
                src="SB3Ail01.svg",
                height=styles.Size.EXTRA_LARGE.value,
                width="auto"),
        # rx.cond(
        #     CondState.show,
        rx.heading("Edgar Zarate", size="7", weight="bold"),
        # rx.heading("Dante", size="7", weight="bold"),
        # ),
        # on_click=CondState.change,
        align_items="center"
    )


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    """ Navbar component: Navbar icon item """
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
            style=styles.subtitle_style,
        ),
        href=url
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    """ Navbar component: Navbar menu item"""
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
            style=styles.subtitle_style,
        ),
        href=url,
    )
