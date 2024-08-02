import reflex as rx
MAX_WIDTH="600px"
import sys
from enum import Enum

STYLESHEETS=["https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
            "https://fonts.googleapis.com/css?family=Comfortaa:wght@500&display=swap"]

class Font(Enum):
    Default="Poppins"
    Title="Poppins"
    Logo="Comfortaa"
    
class FontWeight(Enum):
    light="300"
    medium="500"

class Size(Enum):
    Small= "0.5em"
    Medium= "0.8em"
    Defualt= "1em"
    Big= "2em"
    
class Color(Enum):
    Primary ="#14A1F0"
    Secondary="#087ec4"
    Background="#0C141D"
    Content="#171F26"

class TextColor(Enum):
    Header="#F1F2F4"
    Body="#C3C7CB"
    Footer="#A3ABB2"


BASE_STYLE={
    "font_family": Font.Default.value,
    "font_weight": FontWeight.light.value,
    "background_color":Color.Background.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding": Size.Small.value,
        "border_radius":Size.Medium.value,
        "spacing":"2",
        "color":TextColor.Header.value,
        "background_color":Color.Content.value,
        "text_align":"start",
        "white_space":"normal",
        "_hover":{"background_color": Color.Secondary.value},

    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

button_title_style=dict(
    font_size=Size.Defualt.value,
    color=TextColor.Header.value

)

button_body_style=dict(
    font_size=Size.Medium.value,
    color=TextColor.Body.value

)

title_style=dict(
    width="100%",
    padding_top=Size.Defualt.value,
    color=TextColor.Header.value
)

navbar_title_style=dict(
    font_family= Font.Logo.value,
    font_weight= FontWeight.medium.value,
    font_size="1.5em",
    display= "flex",  # Use flex instead of inline-flex
    alignItems= "center"  # Ensure items are centered vertically
)