import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles import styles
from link_bio.styles.colors import Color

# class CondState(rx.State):
#     show: bool = True
#     def change(self):
#         self.show = not (self.show)

def navbar_logo()->rx.Component:
    return rx.hstack(
        rx.image(src="SB3Ail01.svg", height=Size.EXTRA_LARGE.value, width="auto"),
        # rx.cond(
        #     CondState.show,
            rx.heading("Edgar Zarate",size="7", weight="bold"),
            # rx.heading("Dante", size="7", weight="bold"),
        # ),
        # on_click=CondState.change,
        align_items="center"
    ),

def navbar_icons_item(text: str, icon: str, url:str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text,size="4",weight="medium"),
            style=styles.subtitle_style,
        ),
        href=url
    )

def navbar_icons_menu_item(text: str, icon: str, url: str ) -> rx.Component:
    return  rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
            style=styles.subtitle_style,
        ),
        href=url,
    )



def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                navbar_logo(),
                rx.hstack(
                    navbar_icons_item("Bio","home","/#"),
                    navbar_icons_item("Proyectos","gallery-vertical-end","/#"),
                    navbar_icons_item("Contacto","at-sign","/#"),
                    spacing="5",
                ),
                justify="between",
                align_items="center"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                navbar_logo(),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu"), size=50),
                    rx.menu.content(
                        navbar_icons_menu_item("Bio","home","/#"),
                        navbar_icons_menu_item("Proyectos","gallery-vertical-end","/#"),
                        navbar_icons_menu_item("Contacto","at-sign","/#"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=styles.navbar_style
    )