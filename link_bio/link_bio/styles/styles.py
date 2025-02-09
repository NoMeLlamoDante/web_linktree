""" Webpages Styles """
from enum import Enum
import reflex as rx
from link_bio.styles.colors import Color

# Constants for styling

# Spacing constants


class Size(Enum):
    """ Text size """
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    NORMAL = "1em"
    NORMAL_LARGE = "1.5em"
    SUBTITLE = "1.3em"
    LARGE = "2em"
    EXTRA_LARGE = "3em"


# Styles for all elements
BASE_STYLE = {
    "background": Color.BLACK,
    "color": Color.WHITE,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background": Color.GREEN,
        "color": Color.WHITE,
        "_hover": {
            "background": Color.LIGHT_GREY,
            "color": Color.WHITE,
        }
    },
}

button_tittle_style = {
    "font-size": "1.5em",
    "font-weight": "bold",
}

button_body_style = {
    "font-size": Size.SMALL.value,
    "font-weight": "bold",
}

title_style = dict(
    font_size=Size.LARGE.value,
    justify_content="center",
    text_align="center",
    width="100%",
    color=Color.LIGHT_GREEN,
    padding_y=Size.MEDIUM.value,
)

subtitle_style = dict(
    font_size=Size.SUBTITLE.value,
    color=Color.WHITE,
)

principal_style = dict(
    font_size=Size.EXTRA_LARGE.value,
    justify_content="center",
    width="100%",
    color=Color.LIGHT_GREEN,
    padding_y="0.5rem",
)

text_style = dict(
    font_size=Size.NORMAL.value,
    jusify_content="right",
    width="100%",
    color=Color.WHITE,
)

navbar_style = dict(
    align_items="center",
    position="sticky",
    padding_x=Size.LARGE.value,
    padding_y=Size.SMALL.value,
    top="0px",
    width="100%",
    background=Color.GREEN,
    z_index=100
)

padding = dict(
    padding_y=Size.NORMAL.value,
)

logo = dict(
    width="50px",
    background=Color.GREEN,
)
