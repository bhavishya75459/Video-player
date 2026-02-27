from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from jnius import autoclass
from android.runnable import run_on_ui_thread
from kivymd.toast import toast as t
from kivy.core.clipboard import Clipboard

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1

    MDLabel:
        text: "Simple KivyMD AdMob App"
        halign: "center"
        pos_hint: {"center_y": 0.6}
        theme_text_color: "Primary"

    MDLabel:
        text: "Banner Ad will show at bottom"
        halign: "center"
        pos_hint: {"center_y": 0.5}
'''

# Android AdMob Setup
if platform == "android":
    try:
         AdMobAdapter = autoclass("com.google.ads.mediation.admob.AdMobAdapter")
         AdSize = autoclass('com.google.android.gms.ads.AdSize')
         AdRequestBuilder = autoclass('com.google.android.gms.ads.AdRequest$Builder')
         MobileAds = autoclass('com.google.android.gms.ads.MobileAds')
         PythonActivity = autoclass('org.kivy.android.PythonActivity')
         FrameLayoutParams = autoclass('android.widget.FrameLayout$LayoutParams')        
    
        
    except Exception as e:
        t(f'p:-{e}')
        Clipboard.copy(str(e))

    @run_on_ui_thread
    def toasts(a,*args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        toast=autoclass('android.widget.Toast')
        string=autoclass('java.lang.String')        
        c=PythonActivity.mActivity
        s=string(str(a))
        toast.makeText(c,s,toast.LENGTH_SHORT).show()

    @run_on_ui_thread
    def show_banner():
        try:            
            activity = PythonActivity.mActivity
            MobileAds.initialize(activity)
    
            adview = AdView(activity)
            adview.setAdSize(AdSize.BANNER)
    
            # ✅ Test Banner Ad Unit ID
            adview.setAdUnitId("ca-app-pub-7264801834502563/6725695296")
    
            adRequest = AdRequestBuilder().build()
            adview.loadAd(adRequest)
    
            params = FrameLayoutParams(
                FrameLayoutParams.MATCH_PARENT,
                FrameLayoutParams.WRAP_CONTENT
            )
    
            activity.addContentView(adview, params)

        except Exception as e:
            toasts(str(e))
            Clipboard.copy(str(e))
class AdApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        if platform == "android":
            show_banner()


AdApp().run()
