from pybbmini.base import *


class Buzzer:
    def __init__(self, sender):
        self.__verbose = True
        self.__sender = sender
        

    def melody(self, index=0):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = BUZZER
        command[PACKET_INDEX.DATA0] = BUZZER_MELODY
        command[PACKET_INDEX.DATA1] = index

        # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            print(f'[BUZZER]')
        
    def tone(self, note, duration=1000):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = BUZZER
        command[PACKET_INDEX.DATA0] = BUZZER_NOTE
        command[PACKET_INDEX.DATA1] = note
        # a를 상위 1바이트와 하위 1바이트로 분리합니다.
        ah = duration >> 8
        al = duration & 0xff
        command[PACKET_INDEX.DATA2] = ah
        command[PACKET_INDEX.DATA3] = al

        # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            print(f'[BUZZER]')

    def play(self, tune):
        for el in tune:
            l = el.split(':')
            d = int(1000/int(l[1]))
            self.tone(Note.dict[l[0]], d)