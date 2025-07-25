from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.video import Video

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDLabel:
            text: "KivyMD Video Player"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1

        Video:
            id: video_player
            source: "assets/v1.mp4"
            state: "play"
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: True
            size_hint_y: 0.8

        MDRaisedButton:
            text: "Play / Pause"
            pos_hint: {"center_x": 0.5}
            on_release: app.toggle_video()
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def toggle_video(self):
        player = self.root.ids.video_player
        if player.state == 'play':
            player.state = 'pause'
        else:
            player.state = 'play'

MainApp().run()
