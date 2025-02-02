import reflex as rx
from link_bio.componentes.title import title, subtitle
from link_bio.componentes.card import card_study
from link_bio.componentes.text import studies_data

escuelas = list(studies_data.keys())

itvh = [escuelas[0]]
itvh_studios = studies_data.get(itvh[0])
itvh.append(itvh_studios)

cecati = [escuelas[1]]
cecati_studios = studies_data.get(cecati[0])
cecati.extend(cecati_studios)

ifortab = [escuelas[2]]
ifortab_studios = studies_data.get(ifortab[0])
ifortab.extend(ifortab_studios)

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
            itvh[0], itvh[1]
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
            cecati[0], cecati[1], cecati[2], cecati[3]
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
            ifortab[0], ifortab[1], ifortab[2], ifortab[2]
        ),
        width=rx.breakpoints(initial="90%", sm="60%"),
    ),