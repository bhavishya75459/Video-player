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
import threading

kv='''
Manager:
    Fir:
<Fir>:
    name:'home'   
    MDIconButton:
        icon:'plus'   
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:app.o()
        
    MDTopAppBar:
        id:ta1
        title:'HAR HAR MAHADEV'      
        pos_hint:{'top':1}






'''




class Manager(ScreenManager):
    pass
    
class Fir(Screen):
    pass
    
class Demo(MDApp):
    def build(self):
        self.c=True
        self.b=Builder.load_string(kv)
        return self.b
        
    def o(self):
        try:
            threading.Thread(target=self.s,daemon=True).start()
        except Exception as e:
            toast(e)            
            

    def s(self):
        try:  
            Clock.schedule_once(lambda x:self.n())       
                          
        except Exception as e:
            Clock.schedule_once(lambda x: toast(str(e)))
            
    def n(self):
        try:
            if not self.c:
                self.b.get_screen('home').ids.ta1.title='HAR HAR MAHADEV'   
            else:
                self.b.get_screen('home').ids.ta1.title='JAI MAHAKAL'                                                        
            self.c= not self.c
                                                              
        except Exception as e:
            toast('hs')                                   
                                                      
                              
            
            
Demo().run()

