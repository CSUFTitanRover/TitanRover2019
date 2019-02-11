from finalimu.msg import fimu
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import *
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import random
import rospy
import random

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.main_text = Label(text="Initial Value = None")
        self.arr = Image(source='t.png')
        self.add_widget(self.main_text)
        self.add_widget(self.arr)
        rospy.init_node('listener', anonymous=True)
        Clock.schedule_interval(self.listener, .5)
        

    def update(self, data):
        self.main_text.text = str(data.yaw.yaw)
        self.arr.rotation = data.yaw.yaw

    def listener(self, dt):
        rospy.Subscriber("imu", fimu, self.update)
    

class MyApp(App):
    def build(self):
        return MainView()

MyApp().run()
