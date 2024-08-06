import reflex as rx
import sys
sys.path.append(r'C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\frontend')
from styles import BASE_STYLE,STYLESHEETS
sys.path.append(r'C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend')
from backend.api import hello,live
from pages import courses,index


app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS
)

app.api.add_api_route("/hello",hello)
app.api.add_api_route("/live/{user}",live)