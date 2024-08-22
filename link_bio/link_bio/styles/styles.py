import reflex as rx
from enum import Enum
from link_bio.styles.colors import Color

#Constants for styling

    
#Spacing constants
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    NORMAL = "1em"
    NORMAL_LARGE = "1.5em"
    SUBTITLE = "1.3em"
    LARGE = "2em"
    EXTRA_LARGE = "3em"
    
# Styles for all elements
BASE_STYLE = {
    "background":Color.BLACK,
    "color":Color.WHITE,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background": Color.GREY,
        "color" : Color.WHITE, 
        "_hover": {
            "background": Color.GREEN,
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
    font_size = Size.LARGE.value,
    justify_content = "center",
    text_align = "center",
    width = "100%",
    color = Color.LIGHT_GREEN,
    padding_y = Size.MEDIUM.value,
)

subtitle_style = dict(
    font_size = Size.SUBTITLE.value,
    color = Color.WHITE,
)

text_style = dict(
    font_size = Size.NORMAL.value,
    jusify_content = "right",
    width = "100%",
    color = Color.WHITE,
)

navbar_style = dict(
    align_items="center",
    position = "sticky",
    padding_x = Size.LARGE.value,
    padding_y = Size.SMALL.value,
    top = "0px",
    width ="100%",
    background = Color.GREEN,
    
)

padding = dict(
    padding_y=Size.SMALL.value,
)