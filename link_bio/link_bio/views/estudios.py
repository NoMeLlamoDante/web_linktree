import reflex as rx
from link_bio.componentes.title import title, subtitle

def estudios() -> rx.Component:
    return rx.vstack(
        title("Estudios"),
        # ITVH
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="itvh-logo.png",
                    width="100%",
                    max_width = "400px",
                    height="auto",
                    border_radius = "30px",
                    border= "5px, solid #004638",
                    background= "#FFFFFF",
                ),
                width = "20%",
            ),
            rx.vstack(
                subtitle("Instituto Tecnológico de Villahermosa"),
                rx.text("2011-2016", weight="medium", align="center", as_="label"),
                rx.text("Ingeniería en Sistemas Computacionales", weight="light"),
                width = "80%",

            ),
            align="center",
            justify="center",
            width="100%",
        ),
        rx.divider(),
        # Cecati 95
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="cecati-95-logo.png",
                    width="100%",
                    max_width = "400px",
                    height="auto",
                    border_radius = "50%",
                    border= "5px, solid #004638",
                    background= "#FFFFFF",
                ),
                width = "20%",
            ),
            rx.vstack(
                subtitle("Centro de capacitación para el Trabajo Industrial No. 95"),
                rx.list.unordered(
                    rx.list.item("Sistemas embebidos Microcontrolados para el control electrónico"),
                    rx.list.item("Sistemas electrónicos y de control analógicos y digitales"),
                    rx.list.item("Reparación de tarjetas de control electrónico"),
                ),
                width="80%",
            ),
            align="center",
            justify="center",
            width="100%",
        ),
        rx.divider(),
        # Ifortab 
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="Ifortab-logo.png",
                    width="100%",
                    max_width = "400px",
                    height="auto",
                    border_radius = "30px 30px",
                    border= "5px, solid #004638",
                ),
                width = "20%",
            ),
            rx.vstack(
                subtitle("Instituto de Formación para el trabajo"),
                rx.list.unordered(    
                    rx.list.item("Python Basico"),
                    rx.list.item("Python Intermedio"),
                    rx.list.item("Python avanzado"),
                ),
                width= "80%",
            ),
            align="center",
            justify="center",
            width="100%",
        ),
            

    )