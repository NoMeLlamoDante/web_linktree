import link_bio.styles.styles as styles
import reflex as rx

def link_button(label: str, url: str, icon:str = None) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(icon if icon else "external-link"),
                rx.text(label, style=styles.button_tittle_style), 
                widht="100%"),
            ),
        href=url,
        is_external=True,
        width="100%",
    )
