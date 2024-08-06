import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\frontend")
from styles import Size

def link_icon(url:str,tag:str)->rx.Component:
    return rx.link(
        rx.icon(
            tag=tag,
            width=Size.Big.value,
            height=Size.Big.value,
            margin=Size.Medium.value
        ),
        href= url,
        is_external=True
    )
