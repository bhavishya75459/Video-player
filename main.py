from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'

        VideoPlayer:
            id: video_player
            source: "assets/v1.mp4"
            state: "play"
            options: {"eos": "loop"}
            allow_stretch: True
            size_hint_y: 0.9

        MDRaisedButton:
            text: "Play/Pause"
            pos_hint: {"center_x": 0.5}
            on_release: app.toggle_video()
'''

class MainApp(MDApp):
    def build(self):
        try:
            return Builder.load_string(KV)
        except Exception as e:
            toast(f"Load error: {e}")
            return Builder.load_string('''
MDScreen:
    MDLabel:
        text: "Video load failed."
        halign: "center"
''')

    def toggle_video(self):
        try:
            player = self.root.ids.video_player
            player.state = "pause" if player.state == "play" else "play"
        except Exception as e:
            toast(f"Toggle error: {e}")

MainApp().run()
