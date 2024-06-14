import reflex as rx
from link_bio.componentes.link_button import link_button

def links() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                link_button("Github","https://github.com/NoMeLlamoDante"),
                link_button("linkedin","https://www.linkedin.com/in/edgar-zarate-61285bba/"),
                link_button("pokeword search","https://pokewordsearch-dante.herokuapp.com/"),
                width="100%",
            )
        )
    )