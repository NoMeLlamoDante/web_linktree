import reflex as rx
import datetime
import link_bio.styles.styles as styles


def footer() -> rx.Component:
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