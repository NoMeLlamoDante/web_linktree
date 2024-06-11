import reflex as rx

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Dante", size="7", weight="bold"),
            rx.heading("NoMeLlamoDante", size="3",weight="light", padding=".5rem"),
            justify="between",
            position="sticky",
            background="grey",
            padding="1rem",
        ),
    )

app = rx.App()
app.add_page(index)
app._compile()