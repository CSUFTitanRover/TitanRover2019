import socket

def SetModeAndIP():
    mode = None
    ip = None
    good = False
    while not good:
        mode = raw_input("Mode (\"dev\" or \"prod\"): ")
        if mode == "dev" or mode == "prod":
            good = True
    if mode == "prod":
        ip = '192.168.1.2'
    else:
        ip = AutoGrabIP()
    print "Database IP:", ip
    return mode, ip

# Returns the IP address string of the machine executing this instruction
def AutoGrabIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return str(ip)
