""" Web module: Title """
import reflex as rx
from link_bio.styles import styles


def title(text: str) -> rx.Component:
    """ Reflex component: title"""
    return rx.heading(
        text,
        style=styles.title_style,
    )


def subtitle(text: str) -> rx.Component:
    """ Reflex component: subtitle"""
    return rx.heading(
        text, 
        style=styles.subtitle_style,
    )


def principal(text: str) -> rx.Component:
    """ Reflex component: Principal"""
    return rx.heading(
        text,
        style=styles.principal_style
    )
