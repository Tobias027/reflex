import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\styles")
from styles import Font,FontWeight,title_style

def title(text)->rx.Component:
    return rx.heading( 
                text,
                style=title_style,
                size="7",
                font_family= Font.Default.value,
                font_weight= FontWeight.medium.value
    )