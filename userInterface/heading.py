from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock
import rospy
from finalimu.msg import fimu

import random

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.main_text = Label(text="Initial Value = None")
        self.add_widget(self.main_text)
        rospy.init_node('listener', anonymous=True)
        Clock.schedule_interval(self.listener, .5)
        

    def update(self, data):
        self.main_text.text = str(data.yaw.yaw)#"Next Value = " + str(random.randint(0,200))

    def listener(self, dt):
        rospy.Subscriber("imu", fimu, self.update)
    

class MyApp(App):
    def build(self):
        return MainView()

MyApp().run()
