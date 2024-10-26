import reflex as rx
from link_bio.componentes.title import title
import link_bio.componentes.text as text
from link_bio.styles.styles import Size

def card_job(place: str, period: str, resume: str) -> rx.Component:
    return rx.card(
        rx.heading(place),
        rx.text(period, size="2"),
        rx.text(resume),
        variant="ghost",
        padding_y=Size.NORMAL.value
    )

def experiencia() -> rx.Component:
    return rx.section(
        title("Experiencia Laboral"),
        card_job("CEMATAB","2016",text.cematab_job),
        card_job("ALHEC","2017-2023",text.alhec_job),
        card_job("Freelance","2023-2024",text.freelance_job),
        width=rx.breakpoints(initial="90%", sm="60%"),
    )