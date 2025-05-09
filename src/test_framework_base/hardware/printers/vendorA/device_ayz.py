import vendorA
from ..printer_interface import Printer_I

# glue class used to implement interface by utilizing method in specific device driver
class DeviceAYZ(Printer_I):
    def __init__(self, prefix:str):
        self.driver = vendorA.DeviceAYZ(prefix) 

    def send_msg(self, msg):
        self.driver.print_msg(msg)