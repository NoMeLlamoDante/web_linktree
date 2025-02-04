import reflex as rx
from link_bio.componentes.title import title
from link_bio.componentes.text import experience_data
from link_bio.styles.styles import Size

def card_job(place: str, period: str, resume: str) -> rx.Component:
    return rx.card(
        rx.heading(place),
        rx.text(period, size="2"),
        rx.text(resume),
        variant="ghost",
        padding_y=Size.NORMAL.value
    )

cematab = experience_data['cematab']
alhec = experience_data['alhec']
freelance = experience_data['freelance']

def experiencia() -> rx.Component:
    return rx.section(
        title("Experiencia Laboral"),
        card_job(cematab['name'], cematab['period'], cematab['resume']),
        card_job(alhec['name'], alhec['period'], alhec['resume']),
        card_job(freelance['name'], freelance['period'], freelance['resume']),
        width=rx.breakpoints(initial="90%", sm="60%"),
    )