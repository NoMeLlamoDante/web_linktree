""" Web section: Footer  """
import datetime
import reflex as rx
from link_bio.styles import styles


def footer() -> rx.Component:
    """ Reflex component: Footer section"""
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            width="50px"
        ),
        rx.text(
            "learning to dream in code",
            font_size=styles.Size.MEDIUM.value,
        ),
        rx.text(
            f"2023-{datetime.datetime.now().year}",
            font_size=styles.Size.MEDIUM.value,
        ),
        width="100%",
        align="center",
    )
