import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", width="50px"),
        rx.text("learning to dream in code"),
        rx.text(f"2023-{datetime.datetime.now().year}"),
        width="100%",
        align="center",
    )