import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.image(src="favicon.ico", width="50px"),
    )