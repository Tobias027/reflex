import reflex as rx
import sys
sys.path.append(r'C:\Users\caste\Desktop\PYTHON2\desarrolloweb\frontend\backend')
from backend.api import live

class State(rx.State):
    
    is_live:bool
    
    async def check_live(self):
        self.is_live= await live("Mouredev")