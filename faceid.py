# Import kivy dependencies first

from  kivy.app import App

# Import kivy UX component

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button 
from kivy.uix.label import Label

# Import other kivy stuff

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# Import other dependencies 
import tensorflow as tf
import numpy as np
import os 
from layers import L1Dist
import cv2

# Build APP and Layout

class CamApp(App):
    
    def build(self):
        # Main layout component
        self.img1 = Image(size_hint=(1,.8))
        self.button = Button(text="verify",size_hint=(1,.1))
        self.verification = Label(text="Verification unverified",size_hint=(1,.1))
        
        # Add items to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widegt(self.img1)
        layout.add_widget(self.button)
        layout.add_widget(self.verification)
        
        return layout
    
if __name__ == '__main__':
    CamApp().run()
