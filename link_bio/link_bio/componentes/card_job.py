""" web module: card job """
import reflex as rx
from link_bio.styles.styles import Size


def card_job(place: str, period: str, resume: str) -> rx.Component:
    """ Reflex component: card_job """
    return rx.card(
        rx.heading(place),
        rx.text(period, size="2"),
        rx.text(resume),
        variant="ghost",
        padding_y=Size.NORMAL.value
    )
