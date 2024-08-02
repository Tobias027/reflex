import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\frontend")
from styles import Size,TextColor,Color,navbar_title_style


def navbar()->rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("Tobi",color=Color.Primary.value),
            rx.text("Caste",color=Color.Secondary.value),
            style=navbar_title_style
            ),
        position="sticky",
        bg=Color.Content.value,
        padding_x=Size.Defualt.value,
        padding_y=Size.Small.value,
        z_index="999",
        top="0"
    )