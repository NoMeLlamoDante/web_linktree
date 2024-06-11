import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
            rx.heading("Dante", size="7", weight="bold"),
            rx.heading("Edgar Zarate", size="3",weight="light", padding=".5rem"),
            justify="between",
            position="sticky",
            background="grey",
            padding="1rem",
            width="100%",
        )