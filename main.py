from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button


class VideoPlayerApp(App):

    def build(self):

        root = BoxLayout(orientation="vertical")

        # Video widget
        self.video = Video(
            source="assets/v1.mp4",
            state="stop",
            options={"eos": "loop"},
            allow_stretch=True
        )

        # Play button
        play_btn = Button(text="Play Video", size_hint=(1, 0.1))
        play_btn.bind(on_press=self.play_video)

        root.add_widget(self.video)
        root.add_widget(play_btn)

        return root

    def play_video(self, instance):
        self.video.state = "play"


VideoPlayerApp().run()
