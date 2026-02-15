from kivy.app import App
from kivy.uix.video import Video

class VideoPlayerApp(App):
    def build(self):
        return Video(
            source="assets/v1.mp4",
            state="play",
            options={"eos": "loop"}
        )

VideoPlayerApp().run()
