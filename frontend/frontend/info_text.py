import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend")
from styles import Size,Color,TextColor

def info_text(title:str, body:str)->rx.Component:
    return rx.hstack(
        rx.text(
            title,
            style={"fontWeight": "bold", "color": Color.Primary.value}
        ),
        f"{body}",
        style={"font_size":Size.Medium.value, "color":TextColor.Body.value}
    )