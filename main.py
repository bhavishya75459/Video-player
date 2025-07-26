from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: "home"

    MDLabel:
        text: "JAI MAHAKAL"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1  # Laal color
        font_style: "H4"
        pos_hint: {"center_y": 0.5}
'''

class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
