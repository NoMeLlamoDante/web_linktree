""" Webpage section: work experience"""
import reflex as rx
from link_bio.componentes.title import title
from link_bio.data.text import EXPERIENCE_DATA
from link_bio.styles.styles import Size


def card_job(place: str, period: str, resume: str) -> rx.Component:
    """ Reflex component: card_job """
    return rx.card(
        rx.heading(place),
        rx.text(period, size="2"),
        rx.text(resume),
        variant="ghost",
        padding_y=Size.NORMAL.value
    )


cematab = EXPERIENCE_DATA['cematab']
alhec = EXPERIENCE_DATA['alhec']
freelance = EXPERIENCE_DATA['freelance']


def experiencia() -> rx.Component:
    """ Reflex component: work experience section"""
    return rx.section(
        title("Experiencia Laboral"),
        card_job(cematab['name'], cematab['period'], cematab['resume']),
        card_job(alhec['name'], alhec['period'], alhec['resume']),
        card_job(freelance['name'], freelance['period'], freelance['resume']),
        width=rx.breakpoints(initial="90%", sm="60%"),
    )
