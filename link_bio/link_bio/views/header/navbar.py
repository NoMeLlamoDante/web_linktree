""" Web section: navbar """
import reflex as rx
from link_bio.styles import styles
from link_bio.componentes.navbar_items import navbar_logo
from link_bio.componentes.navbar_items import navbar_icons_item
from link_bio.componentes.navbar_items import navbar_icons_menu_item
# class CondState(rx.State):
#     show: bool = True
#     def change(self):
#         self.show = not (self.show)


def navbar() -> rx.Component:
    """ Reflex module: Navbar """
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                navbar_logo(),
                rx.hstack(
                    navbar_icons_item("Bio", "home", "/#"),
                    navbar_icons_item(
                                    "Proyectos",
                                    "gallery-vertical-end",
                                    "/#"),
                    navbar_icons_item("Contacto", "at-sign", "/#"),
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
                        navbar_icons_menu_item("Bio", "home", "/#"),
                        navbar_icons_menu_item(
                                            "Proyectos",
                                            "gallery-vertical-end",
                                            "/#"),
                        navbar_icons_menu_item("Contacto", "at-sign", "/#"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=styles.navbar_style
    )
