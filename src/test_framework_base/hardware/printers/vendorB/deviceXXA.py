import vendorB
from ..printer_interface import Printer_I

# glue class used to implement interface by utilizing method in specific device driver
class DeviceXXA(Printer_I):
    def __init__(self):
        self.driver = vendorB.DeviceXXA() 

    def send_msg(self, msg):
        self.driver.print_msg(msg)