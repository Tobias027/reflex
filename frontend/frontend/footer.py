import reflex as rx
import datetime
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend")
from styles import Size,TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            f"Diseñada gracias a los cursos de Mouredev {datetime.date.today().year}",
            href="https://github.com/mouredev",
            is_external=True,
            color=TextColor.Footer.value
            #margin_top="0pc !important" #sirve 
        ),
        rx.hstack(
            rx.image(
                src="/leo.webp",
                weight="9em",
                height="9em"
            ),
            rx.spacer(),
            rx.image(
                src="/roma.jpeg",
                weight=Size.Big.value,
                height=Size.Big.value
            ),
            rx.spacer(),
            rx.image(
                src="/leo.webp",
                weight=Size.Big.value,
                height=Size.Big.value
            ),
            
        ),
        style={"alignItems": "center", "justifyContent": "center", "width": "100%"},
        margin_bottom=Size.Big,
        padding_bottom=Size.Big, #separa mas la parte de abajo
        padding=Size.Big.value
    )