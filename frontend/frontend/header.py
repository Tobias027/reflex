import reflex as rx
import sys
sys.path.append(r'C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\frontend')
from styles import Size,Color,TextColor,FontWeight,Font
from link_icon import link_icon
from info_text import info_text


def header(details=True, live=False)->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                rx.cond(
                    live,
                    rx.icon_button("calendar")
                ),
                fallback="TC",
                size="7",
                padding="2px",
                border="2px",
                border_color=Color.Primary.value,
                border_radius=Size.Medium.value,
                src="caste.jpeg"
            ),    
            rx.vstack(
                rx.heading(
                    "Tobias Castellarin",
                    size="7",
                    color=TextColor.Header.value,
                    font_family= Font.Default.value,
                    font_weight= FontWeight.medium.value,
                ),
                rx.text(
                    "¡¡Hola 👋 bienvenido a mi primer pagina web!!",
                    margin_top= "0px !important",
                    color=TextColor.Body.value
                ),
            rx.hstack(    
            link_icon(url="https://x.com/mouredev",tag="Twitter"),
            link_icon(url="https://youtube.com/mouredev",tag="Youtube"),
            link_icon(url="https://github.com/mouredev",tag="Github")  
            ),
            align_items="start",
            ),
        spacing=Size.Medium.value
        ),
        rx.flex(
            info_text("1º","año en Licenciatura en Sistemas"),
            rx.spacer(),
            info_text("+6","años estudiando ingles"),
            rx.spacer(),
            info_text("+1","año de experiencia"),
            width="100%"
        ),
        rx.text("soy estudiante de Licenciatura en Sistemas y me especializo en backend como bases de datos, especificamente postgreSQl.",
                color=TextColor.Body),
        spacing=Size.Big.value,
        align_items="start"
    )