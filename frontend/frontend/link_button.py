import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\frontend")
from styles import Size,button_body_style,button_title_style
from title import title
from routes import Route

def link_button(title: str, body: str, url: str,is_external:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="MoveRight",
                    width=Size.Big.value,
                    height=Size.Big.value,
                    margin=Size.Medium.value,
                    alt="arrow"
                ),
                rx.vstack(
                    rx.text(title,style=button_title_style),
                    rx.text(body,style=button_body_style),
                    align_items="start",
                    margin="0em !important",
                    spacing=Size.Small.value
                ),
                align_items="center"  # Asegura que los items en hstack estén alineados centralmente
            ),
            width="100%",
            justify_content="left"
        ),
        href=url,
        is_external=is_external,
        style={"width": "100%"}
    )



def links()->rx.Component:
    return rx.vstack(
    title("Conctactos:"),
    link_button("Facebook","social media y mucho mas que vas poder ver a traves de los canales oficiales", "https://facebook.com",True),
    link_button("WhatsApp","social media", "https://whatsapp.com",True),
    link_button("Cursos gratis","Consulta mis tutoriales para aprender programación", Route.Courses.value,False ),
    style={"width": "100%"}
)
