from pybbmini.base import *


class Display:
    def __init__(self, sender):
        self.__verbose = True
        self.__sender = sender

    def symbol(self, symbol):
        command = NULL_COMMAND_PACKET[:]
        input = symbol.split(":")
        for i, el in enumerate(input):
            b = int(el, 2)    
            # print(bin(b))   # 2진수 문자열 
            input[i] = b
        
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = MATRIX_LED
        command[PACKET_INDEX.DATA0] = DISPLAY_SYMBOL
        command[PACKET_INDEX.DATA1] = input[0]
        command[PACKET_INDEX.DATA2] = input[1]
        command[PACKET_INDEX.DATA3] = input[2]
        command[PACKET_INDEX.DATA4] = input[3]
        command[PACKET_INDEX.DATA5] = input[4]
        command[PACKET_INDEX.DATA6] = 0x00 # R
        command[PACKET_INDEX.DATA7] = 0xFF # G
        command[PACKET_INDEX.DATA8] = 0x00 # B

        # 시리얼 송신
        ret = self.__sender.send(command)

        if self.__verbose:
            # print('[display show] ', ret)
            pass

    def show(self, symbol):
        command = NULL_COMMAND_PACKET[:]
        input = None
        
        if 'Symbol' in str(type(symbol)):
            input = symbol.value.split(":")
            for i, el in enumerate(input):
                b = int(el, 2)    
                # print(bin(b))   # 2진수 문자열 
                input[i] = b
            
            command = NULL_COMMAND_PACKET[:]
            command[PACKET_INDEX.ACTION] = MATRIX_LED
            command[PACKET_INDEX.DATA0] = DISPLAY_SYMBOL
            command[PACKET_INDEX.DATA1] = input[0]
            command[PACKET_INDEX.DATA2] = input[1]
            command[PACKET_INDEX.DATA3] = input[2]
            command[PACKET_INDEX.DATA4] = input[3]
            command[PACKET_INDEX.DATA5] = input[4]
            command[PACKET_INDEX.DATA6] = 0x00 # R
            command[PACKET_INDEX.DATA7] = 0xFF # G
            command[PACKET_INDEX.DATA8] = 0x00 # B
        else:
            input = symbol.upper()
            if ord(input) > 64:
                print('CHAR')
                command[PACKET_INDEX.ACTION] = MATRIX_LED
                command[PACKET_INDEX.DATA0] = DISPLAY_CHAR
                command[PACKET_INDEX.DATA1] = ord(input) # 문자를 아스키 코드 값으로 변환
                command[PACKET_INDEX.DATA2] = 0x00 # R
                command[PACKET_INDEX.DATA3] = 0xFF # G
                command[PACKET_INDEX.DATA4] = 0x00 # B
            else:
                print('NUMBER')
                command = NULL_COMMAND_PACKET[:]
                command[PACKET_INDEX.ACTION] = MATRIX_LED
                command[PACKET_INDEX.DATA0] = DISPLAY_NUM
                command[PACKET_INDEX.DATA1] = int(input)
                command[PACKET_INDEX.DATA2] = 0x00 # R
                command[PACKET_INDEX.DATA3] = 0xFF # G
                command[PACKET_INDEX.DATA4] = 0x00 # B

        # 시리얼 송신
        ret = self.__sender.send(command)

        if self.__verbose:
            # print('[display show] ', ret)
            pass
        
    def color(self, color):
        # color : tuple
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = MATRIX_LED
        command[PACKET_INDEX.DATA0] = DISPLAY_COLOR
        command[PACKET_INDEX.DATA1] = color[0] 
        command[PACKET_INDEX.DATA2] = color[1] 
        command[PACKET_INDEX.DATA3] = color[2] 

         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            # print('[display show] ', ret)
            pass

    def clear(self):
        # color : tuple
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = MATRIX_LED
        command[PACKET_INDEX.DATA0] = DISPLAY_COLOR
        command[PACKET_INDEX.DATA1] = 0x00
        command[PACKET_INDEX.DATA2] = 0x00
        command[PACKET_INDEX.DATA3] = 0x00
         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            # print('[display show] ', ret)
            pass

    def effect(self, idx=0):
        # color : tuple
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = MATRIX_LED
        command[PACKET_INDEX.DATA0] = DISPLAY_EFFECT
        command[PACKET_INDEX.DATA1] = idx  # 효과번호
        command[PACKET_INDEX.DATA2] = 10 # 딜레이 시간(사용안함)

         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            # print('[display effect] ', ret)
            pass