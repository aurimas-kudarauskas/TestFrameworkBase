from abc import ABC, abstractmethod

class Printer_I(ABC):

    @abstractmethod
    def send_msg(self, msg:str):
        #Method should send a message to the printer
        pass