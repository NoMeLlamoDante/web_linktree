import reflex as rx

def link_button(label: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(label),
        href=url,
        is_external=True,
    )
