from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage,CoreImage
from kivymd.uix.textfield import MDTextField
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
from kivy.metrics import dp
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.utils import platform
from android.storage import primary_external_storage_path
from kivy.core.clipboard import Clipboard
import os
import re
import datetime
import time
import sqlite3
from kivy.clock import Clock
import io
import base64
import webbrowser
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from jnius import JavaException
from kivy.properties import StringProperty
import threading


kv='''
Manager:
    Fir:
    Sec:
        
<Fir>:
    name:'S1'
    md_bg_color:1,0,0,1
        
    MDBottomNavigation:
        id:bn1    
        #panel_color:1,1,1,1
        #selected_color_indicator:0,0,0,0
        MDBottomNavigationItem:
            name:'ns1'  
            text:'home'  
            icon:'home'
            MDCard:
                id:mdc1
                pos_hint:{'center_x':0.5,'center_y':0.45}
                size_hint:1,0.9 
                radius:[30,30,30,30]            
                elevation:8      
                RecycleView:
                    id:rv1
                    viewclass:'ImgCard'
                    RecycleBoxLayout:
                        default_size: None, dp(260)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        spacing:10
                        padding:10
                        orientation: "vertical"
            
            
    
            MDTopAppBar:
                id:ta1
                title:'OUR APP'
                anchor_title:'left'
                pos_hint:{'top':1}
                #md_bg_color:1,1,1,1
                specific_text_color:1,0,0,1
                right_action_items: [["white-balance-sunny", lambda x: app.theme_change(self)],["update",lambda x:app.add()]]
                
        MDBottomNavigationItem:
            name:'ns2'
            text:'setting'
            icon:'cog'
            


'''

class Manager(ScreenManager):
    pass
    
class Fir(Screen):
    pass
     
class Sec(Screen):
    pass
    
class ImgCard(MDBoxLayout):
    try:
        img = StringProperty('')
    
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.orientation = 'vertical'
            self.spacing = dp(5)
            self.size_hint_y = None
            self.height = dp(220)        
         
            self.image = AsyncImage(size_hint=(1,1),
                allow_stretch=True,
                keep_ratio=False            
            )
            self.add_widget(self.image)        
            self.bu1=MDIconButton(icon='download',pos_hint={'center_x':0.9,'center_y':0.1})                
            self.add_widget(self.bu1)       
            self.bu1.bind(on_press=self.dow)        
    
        def on_img(self, instance, value):      
            self.image.source = value
            self.image.opacity=0
            anim=Animation(opacity=1,duration=3)
            anim.start(self.image)
    except Exception as e:
        toast(str(e))     

    def dow(self,*args):
        try:
            url=f'{self.img}'          
            threading.Thread(target=self.down,args=(self.img,),daemon=True).start()
            
        except Exception as e:
            toast(str(e))                                                  
    def down(self,va):
        try:
             path=primary_external_storage_path()               
             dow_path=f'{path}/Download/y_t'
             os.makedirs(dow_path,exist_ok=True)
             response=requests.get(va)
             if response.status_code==200:
                 with open(f'{dow_path}/a_{random.randint(0,107360373)}.png','wb') as f:
                     f.write(response.content)
                     Clock.schedule_once(lambda x: toast('DOWNLOADED')) 
                     
                 
             
                                                    
        except Exception as e:
            Clock.schedule_once(lambda x: toast(str(re)))    
            Clipboard.copy(str(e))                                                                                        

class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"  # Options are "Light" or "Dark"
        self.theme=False
        self.b=Builder.load_string(kv)
        return self.b
        
    def on_start(self):
        try:
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except Exception as e:
            pass
                            
        list=[]
        for i in range(100):
            image_url = f"https://picsum.photos/600/300?random={i}"
            list.append({'img':image_url})
        self.b.get_screen('S1').ids.rv1.data=list
                 
    def delete(self):
        self.b.get_screen('S1').ids.rv1.data=[]           
       
    def add(self):        
        list=[]                 
        for i in range(100):
            unique=random.randint(0,1000000000)
            image_url = f"https://picsum.photos/600/300?random={unique}"
            list.append({'img':image_url})
        self.b.get_screen('S1').ids.rv1.data=list      
        
    def theme_change(self,a):     
        if self.theme:
            self.b.get_screen('S1').ids.bn1.panel_color=0,0,0,1
            self.theme_cls.primary_palette = "Teal"
            self.theme_cls.theme_style = "Dark"      
            self.theme = not self.theme
        else:
            self.theme_cls.primary_palette = "Red"
            self.theme_cls.theme_style = "Light"   
            self.b.get_screen('S1').ids.bn1.panel_color=1,1,1,1
            self.b.get_screen('S1').ids.ta1.md_bg_color=1,1,1,1
            self.theme = not self.theme               
                  

App().run()
