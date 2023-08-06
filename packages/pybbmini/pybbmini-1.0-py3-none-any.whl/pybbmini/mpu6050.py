from pybbmini.base import *
import struct

class MPU:
    def __init__(self, sender, sda=14, scl=21):
        self.__verbose = True
        self.__sender = sender
        self.__scl = scl
        self.__sda = sda
        
    def get(self):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = MPU_ACTION

        # 시리얼 송신
        ret = self.__sender.send(command)
        ax = ret[RETURN_PACKET.DATA1: RETURN_PACKET.DATA5]
        ay = ret[RETURN_PACKET.DATA5: RETURN_PACKET.DATA9]
        az = ret[RETURN_PACKET.DATA9: RETURN_PACKET.DATA13]
        ax = int(struct.unpack('f', bytearray(ax))[0])
        ay = int(struct.unpack('f', bytearray(ay))[0])
        az = int(struct.unpack('f', bytearray(az))[0])
        return (ax, ay, az)
    
