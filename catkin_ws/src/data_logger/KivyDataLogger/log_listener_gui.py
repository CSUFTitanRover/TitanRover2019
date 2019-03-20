#!/usr/bin/env python
import rospy
import collections
import subprocess
from os import _exit

# rosout msg format
from rosgraph_msgs.msg import Log

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App

import threading


# Get list of nodes from ROS (to populate the dropdown)
system = subprocess.check_output("rosnode list", shell=True).strip().decode("utf-8")
dropdown_list = system.split('\n')
dropdown_list.insert(0,'all')

nodeName = dropdown_list # Listens to these nodes


# Initialize Circular Lists
InfoLogList = collections.deque(maxlen=5)
WarnLogList = collections.deque(maxlen=5)
DebugLogList = collections.deque(maxlen=5)
ErrorLogList = collections.deque(maxlen=5)
FatalLogList = collections.deque(maxlen=5)

def ClearDeques():
    InfoLogList.clear()
    WarnLogList.clear()
    DebugLogList.clear()
    ErrorLogList.clear()
    FatalLogList.clear()


# Data structure for Log Messages
class LogMsg(object):
    msg=''
    name=''
    file=''
    level=0



# Add subscribed data to Lists
def AddToList(data):
    temp = LogMsg()
    temp.msg = data.msg
    temp.name = data.name
    temp.file = data.file
    temp.level = data.level


    if data.level == 2:
        InfoLogList.append(temp)
    elif data.level == 4:
        WarnLogList.append(temp)
    elif data.level == 1:
        DebugLogList.append(temp)
    elif data.level == 8:
        ErrorLogList.append(temp)
    elif data.level == 16:
        FatalLogList.append(temp)


# Create a callback function for the subscriber
def callback(data,qApp):
    
    if data.name in nodeName:                
        AddToList(data)

    #DisplayData()
    qApp.get_dataframe()


def listener():
    qApp = Log_Listener_GuiApp()
    qApp.run()
    
    
    
    


class SelectableRecycleGridLayout(RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)



class Log_Listener_GuiDb(BoxLayout):
    items_list = ObjectProperty(None)
    column_headings = ObjectProperty(None)      

    info_data = ListProperty([])
    warn_data = ListProperty([])
    debug_data = ListProperty([])
    error_data = ListProperty([])
    fatal_data = ListProperty([])

    def __init__(self, **kwargs):
        super(Log_Listener_GuiDb, self).__init__(**kwargs)
        self.column_headings.add_widget(Label(text="Message", bold=True))
        self.column_headings.add_widget(Label(text="Node", bold=True))
        self.column_headings.add_widget(Label(text="File", bold=True))
        self.get_dataframe()

        self.ids.node_spinner.values = dropdown_list

        # Start ROS subscriber thread
        thr = threading.Thread(target=self.start_spin, args=(), kwargs={})
        thr.start()
    
    
    # Dropdown select event
    def set_node(self, node_selected):
        
        global nodeName

        if(node_selected=="all"):
            nodeName = dropdown_list
        else:
            nodeName = [node_selected]

        ClearDeques()


    def start_spin(self):
        # Get the ~private namespace parameters from command line or launch file.
        topic = rospy.get_param('~topic', 'rosout')
        # Create a subscriber with appropriate topic, custom message and name of callback function.
        rospy.Subscriber(topic, Log, callback, callback_args=self)    

        # Wait for messages on topic, go to callback function when new messages arrive.
        rospy.spin()

    def get_dataframe(self):
        
        self.info_data = []
        self.warn_data = []
        self.debug_data = []
        self.error_data = []
        self.fatal_data = []

        
        # Extract and create rows
        row = []
        countrow = 0
        for m in InfoLogList:           
            row.append([m.msg,countrow])
            row.append([m.name,countrow])
            row.append([m.file,countrow])

            countrow += 1
        
        self.info_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True, 'bold' : True} for x in row]


        row = []
        countrow = 0
        for m in WarnLogList:           
            row.append([m.msg,countrow])
            row.append([m.name,countrow])
            row.append([m.file,countrow])

            countrow += 1
        
        self.warn_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True, 'bold' : True} for x in row]



        row = []
        countrow = 0
        for m in DebugLogList:           
            row.append([m.msg,countrow])
            row.append([m.name,countrow])
            row.append([m.file,countrow])

            countrow += 1
        
        self.debug_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True, 'bold' : True} for x in row]


        row = []
        countrow = 0
        for m in ErrorLogList:           
            row.append([m.msg,countrow])
            row.append([m.name,countrow])
            row.append([m.file,countrow])

            countrow += 1
        
        self.error_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True, 'bold' : True} for x in row]


        row = []
        countrow = 0
        for m in FatalLogList:           
            row.append([m.msg,countrow])
            row.append([m.name,countrow])
            row.append([m.file,countrow])

            countrow += 1
        
        self.fatal_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True, 'bold' : True} for x in row]

      

class Log_Listener_GuiApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)    # white background
        self.title = 'Log Listener GUI'
        return Log_Listener_GuiDb()

    def on_stop(self):
        print("Goodbye..")
        rospy.signal_shutdown("Goodbye")
        _exit(0)


if __name__ == "__main__":
    

    # Initialize the node and name it.
    rospy.init_node('log_listener', anonymous = True)
    # Go to the main loop.
    listener()