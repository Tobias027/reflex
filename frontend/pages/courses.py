import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend")
from frontend.navbar_items import navbar
from frontend.header import header
from frontend.link_button import links
from frontend.footer import footer
from frontend.styles import MAX_WIDTH,Size
from frontend.routes import Route

@rx.page(
    route=Route.Courses.value
)
def courses()->rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    links(),
                    max_width=MAX_WIDTH,
                    width="100%",
                    margin_y=Size.Big.value,
                    padding=Size.Big.value
                )
            ),
            align_items="start"
    )


