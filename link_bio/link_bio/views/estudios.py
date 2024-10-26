import reflex as rx
from link_bio.componentes.title import title, subtitle
from link_bio.componentes.card import card_study

def estudios() -> rx.Component:
    return rx.section(
        title("Estudios"),
        #ITVH
        card_study(
            rx.image(
                src="itvh-logo.png",
                width="auto",
                max_height = "300px",
                height="auto",
                border_radius = "15%",
                border= "5px, solid #004638",
                background= "#FFFFFF",
            ),
            "Instituto Tecnológico de Villahermosa",
            "Ingeniería en Sistemas Computacionales",
        ),
        #Cecati
        card_study(
            rx.image(
                src="cecati-95-logo.png",
                width="auto",
                max_height = "300px",
                height="auto",
                border_radius = "50%",
                border= "5px, solid #004638",
                background= "#FFFFFF",
            ),
            "Centro de capacitación para el Trabajo Industrial No. 95",
            "Sistemas embebidos Microcontrolados para el control electrónico",
            "Sistemas electrónicos y de control analógicos y digitales",
            "Reparación de tarjetas de control electrónico"
        ),
        #IFORTAB
        card_study(
            rx.image(
                src="Ifortab-logo.png",
                width="100%",
                max_width = "400px",
                height="auto",
                border_radius = "30px 30px",
                border= "5px, solid #004638",
            ),
            "Instituto de Formación para el trabajo",
            "Python Basico",
            "Python Intermedio",
            "Python avanzado",
        ),
        width=rx.breakpoints(initial="90%", sm="60%"),
    ),