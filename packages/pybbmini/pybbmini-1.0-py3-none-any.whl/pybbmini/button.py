from pybbmini.base import *


class Button:
    def __init__(self, sender, pin):
        self.__verbose = True
        self.__sender = sender
        self.__pin = pin
        self.__name = 'AB' if pin == P99_PIN else ('A' if pin == P6_PIN else 'B')
        

    def isPressed(self):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = BUTTON

        # 시리얼 송신
        ret = self.__sender.send(command)
        
        val = False
        if self.__name == 'AB':
            valA = ret[5]
            valB = ret[6]
            if valA == 1 and valB == 1:
                val = True
            else:
                val = False
        elif self.__name == 'A':
            val = ret[5]
        else:
            val = ret[6]
        
        if self.__verbose:
            # print(f'[BUTTON] {self.__name}:{val}')
            pass

        return True if val == 1 else False

