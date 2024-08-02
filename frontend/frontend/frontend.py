import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend")
from styles import BASE_STYLE,STYLESHEETS
from rxconfig import config
from pages import index,courses

class State(rx.State):
    pass


app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS
)
