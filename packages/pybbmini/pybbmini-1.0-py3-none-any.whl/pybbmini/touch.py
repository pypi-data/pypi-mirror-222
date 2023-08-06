from pybbmini.base import *


class Touch:
    def __init__(self, sender, pin):
        self.__verbose = True
        self.__sender = sender
        self.__name = 'TOUCH_0' if pin == P0_PIN else ('TOUCH_2' if pin == P2_PIN else 'TOUCH_1')
        self.__pin = pin
        

    def isTouched(self):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = TOUCH
        command[PACKET_INDEX.DATA0] = self.__pin
        
        # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            # print(f'[{self.__name}]: ', ret[RETURN_PACKET.DATA0])
            pass

        if self.__name == 'TOUCH_0':
            val_5 =  ret[RETURN_PACKET.DATA1]
            val_6 =  ret[RETURN_PACKET.DATA2]
            return (val_6 <<8 | val_5)
        elif self.__name == 'TOUCH_1':
            val_7 =  ret[RETURN_PACKET.DATA3]
            val_8 =  ret[RETURN_PACKET.DATA4]
            return (val_8 <<8 | val_7)
        else:
            # print('TOUCH_2') # 9 10
            val_9 =  ret[RETURN_PACKET.DATA5]
            val_10 =  ret[RETURN_PACKET.DATA6]
            return (val_10 <<8 | val_9)
