import rospy
from os import system


Class logger:
    def __init__(self, name, line_num):
        self.name = name

    def err(self, err):
        rospy.logerr('['+ self.name + '] ' + err + ' ' + line_num)
    
    def info(self, err):
        rospy.loginfo('['+ self.name + '] ' + err + ' ' + line_nu)

    def fatal(self, err):
        rospy.logfatal('['+ self.name + '] ' + err + ' ' + line_nu)

    def debug(self, err):
        rospy.logdebug('['+ self.name + '] ' + err + ' ' + line_nu)

    def warn(self, err):
        rospy.logwarn('['+ self.name + '] ' + err + ' ' + line_nu)



def main(name):
    while:
        system('clear')
        print(name)



def __init__:
    if sys.argv[0] < 1
        print('Required Arguments not provided')
        exit(1)
    main()

