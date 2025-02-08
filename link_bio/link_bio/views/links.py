""" Web component: Links section"""
import reflex as rx
from link_bio.componentes.link_button import link_button
from link_bio.componentes.title import title
from link_bio.componentes import constants


def links() -> rx.Component:
    """ Reflex component: links section"""
    return rx.vstack(
        title("Links"),
        link_button("Github", constants.GITHUB_URL, "github"),
        link_button("linkedin", constants.LINKEDIN_URL, "linkedin"),
        # link_button(
        #     "pokeword search",
        #     constants.POKESEARCH_URL,
        # ),
        # link_button(
        #     "Youtube",
        #     constants.POKESEARCH_URL,
        # ),
    )
