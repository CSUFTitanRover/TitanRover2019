from finalimu.msg import fimu
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import *
from kivy.graphics import Rotate
from kivy.graphics.context_instructions import Rotate
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import random
import rospy
import random


class Arrow(Widget):
    z_angle = NumericProperty(50)

class HeadingView(Widget):

    arrow = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(HeadingView, self).__init__(**kwargs)

        self.main_text = Label(text="Initial Value = None")
        self.add_widget(self.main_text)

        rospy.init_node('listener', anonymous=True)
        Clock.schedule_interval(self.listener, .5)

    def update(self, data):
        self.main_text.text = str(data.yaw.yaw)
        self.arrow.z_angle = NumericProperty(data.yaw.yaw)

    def listener(self, dt):
        rospy.Subscriber("imu", fimu, self.update)


class Rover_HeadingApp(App):

    def build(self):
        view = HeadingView()
        return view


if __name__ == '__main__':
    Rover_HeadingApp().run()
