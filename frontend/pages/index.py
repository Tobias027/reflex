import reflex as rx
import sys
sys.path.append(r"C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend")
from frontend.navbar_items import navbar
from frontend.header import header
from frontend.link_button import links
from frontend.footer import footer
from frontend.styles import MAX_WIDTH,Size
from frontend.state import State
from frontend.routes import Route


@rx.page(
    on_load=State.check_live
)

def index()->rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(
                        True,
                        State.is_live
                    ),
                    links(),
                    max_width=MAX_WIDTH,
                    width="100%",
                    margin_y=Size.Big.value,
                    padding=Size.Big.value
                )
            ),
            footer(),
            align_items="start"
    )


