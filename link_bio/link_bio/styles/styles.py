import reflex as rx
from enum import Enum

#Constants for styling
MAX_WIDTH = "600px"


#Spacing constants

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    NORMAL = "1em"
    LARGE = "2em"
    EXTRA_LARGE = "3em"
    
# Styles 

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
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
)