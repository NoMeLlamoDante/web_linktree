import reflex as rx
from link_bio.componentes.link_button import link_button
from link_bio.componentes.title import title

def links() -> rx.Component:
    return  rx.vstack(
                title("Links"),
                link_button("Github","https://github.com/NoMeLlamoDante", "github"),
                link_button("linkedin","https://www.linkedin.com/in/edgar-zarate-61285bba/", "linkedin"),
                link_button("pokeword search","https://pokewordsearch-dante.herokuapp.com/"),
            )
    
