# -*-coding:utf-8-*-
import sys
import serial
import time
from pybbmini.base import *
from pybbmini.display import *
from pybbmini.button import *
from pybbmini.buzzer import *
from pybbmini.touch import *
from pybbmini.mpu6050 import *


def delay(ms):
    seconds = ms / 1000.0
    time.sleep(seconds)

class BBBoard:
    def __init__(self, port=None, baud=57600, timeout=2, verbose=True):
        self.__verbose = verbose
        self.__cmdIndex = 1     # 순차적으로 증가

        self.__data0 = None
        self.__data1 = None
        self.__data2 = None
        self.__data3 = None
        self.__data4 = None
        self.__data5 = None
        self.__data6 = None
        self.__data7 = None
        self.__data8 = None
        self.__data9 = None
        self.__data10 = None
        self.__data11 = None
        self.__data12 = None
        self.__data13 = None
        self.__time = time.time()

        self.display = Display(self)
        self.buttonA = Button(self, P6_PIN)
        self.buttonB = Button(self, P5_PIN)
        self.buttonAB = Button(self, P99_PIN)
        self.buzzer = Buzzer(self)
        self.touch0 = Touch(self, P0_PIN)
        self.touch1 = Touch(self, P1_PIN)
        self.touch2 = Touch(self, P2_PIN)
        self.angle = MPU(self)
        
        try:
            if self.__verbose:
                print("\nPython Version %s" % sys.version)

            if not port:
                raise ValueError("Could not find port.")

            sr = serial.Serial(port, baud, timeout=timeout)
            sr.flush()
            self.sr = sr
        except KeyboardInterrupt:
            if self.__verbose:
                print("Program Aborted Before Kamibot Instantiated")
            sys.exit()

    def __get_idx(self):
        self.__cmdIndex = self.__cmdIndex + 1
        if self.__cmdIndex > 255:
            self.__cmdIndex = 1
        return self.__cmdIndex

    def close(self):
        if self.sr.isOpen():
            self.sr.flush()
            self.sr.close()

        if self.__verbose:
            # print("KamibotPi close(): Calling sys.exit(0): Hope to see you soon!")
            pass 
        sys.exit(0)

    def __printHex(self, command):
        print("[", end="")
        for c in command:
            print("%x "%c, end="")
        print("]")

    def __process_return(self):
        data = []
        # 26
        while len(data) < RETURN_PACKET_LENGTH:
            if self.sr.inWaiting():
                c = self.sr.read()
                data.append(ord(c))
            else:
                time.sleep(.001)
                        
        if self.__verbose:
            print('*** return ***')
            # print(data)
            self.__printHex(data)
            # print('return data length {0}'.format(len(data)))

        if len(data) == 20:
            self.__data0 = data[RETURN_PACKET.DATA0]
            self.__data1 = data[RETURN_PACKET.DATA1]
            self.__data2 = data[RETURN_PACKET.DATA2]
            self.__data3 = data[RETURN_PACKET.DATA3]
            self.__data4 = data[RETURN_PACKET.DATA4]
            self.__data5 = data[RETURN_PACKET.DATA5]
            self.__data6 = data[RETURN_PACKET.DATA6]
            self.__data7 = data[RETURN_PACKET.DATA7]
            self.__data8 = data[RETURN_PACKET.DATA8]
            self.__data9 = data[RETURN_PACKET.DATA9]
            self.__data10 = data[RETURN_PACKET.DATA10]
            self.__data11 = data[RETURN_PACKET.DATA11]
            self.__data12 = data[RETURN_PACKET.DATA12]
            self.__data13 = data[RETURN_PACKET.DATA13]
            
            # lower_byte = self.__data0
            # upper_byte = self.__data1
            # analog_value = (upper_byte << 8) + lower_byte
            # print('ANALOG INPUT : ', analog_value);            
        else:
            print(f'Return data error! size={len(data)}')
        
        return data

    # -------------------------------------------------------------------------------------------------------
    #  BLOCK ACTION
    # -------------------------------------------------------------------------------------------------------
    def delay(self, sec):
        """기다리기

        Args:
            sec (float): 초
        Returns:
            None
        """
        time.sleep(sec)

    def __printHex(self, command):
        print("[", end="")
        for c in command:
            print("%x "%c, end="")
        print("]")

    def send(self, command):
        # 패킷 인덱스는 여기서 집어넣는다. 
        command[PACKET_INDEX.INDEX] = self.__get_idx()

        if self.__verbose:
            print("\n *** sendCommand ***")
            self.__printHex(command)
        
        try:
            self.sr.write(bytes(bytearray(command)))
            self.sr.flush()
        except Exception as e:
            print('An Exception occurred!', e)
            return []
        # self.__process_return()
        return self.__process_return()

    def digitalWrite(self, pin, val):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = DIGITAL 
        command[PACKET_INDEX.DATA0] = DIGITAL_OUTPUT 
        command[PACKET_INDEX.DATA1] = pin
        command[PACKET_INDEX.DATA2] = val
        # 시리얼 송신
        ret = self.send(command)
        if self.__verbose:
            # print(f'[DigitalWrite]: ', ret)
            pass
        return 1
    
    def digitalRead(self, pin, mode=PinMode.INPUT):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = DIGITAL 
        command[PACKET_INDEX.DATA0] = mode
        command[PACKET_INDEX.DATA1] = pin
        ret = self.send(command)

        if self.__verbose:
            # print(f'[digitalRead]: ', ret[RETURN_PACKET.DATA1])
            pass
        return ret[RETURN_PACKET.DATA1]

    
    def analogWrite(self, pin, val):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = ANALOG 
        command[PACKET_INDEX.DATA0] = ANALOG_OUTPUT 
        command[PACKET_INDEX.DATA1] = pin
        command[PACKET_INDEX.DATA2] = val  # 0 ~ 100
        print('VAL ', val)
        # 시리얼 송신
        ret = self.send(command)
        if self.__verbose:
            # print(f'[AnalogWrite]: ', ret)
            pass
        return 1

    def analogRead(self, pin):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = ANALOG 
        command[PACKET_INDEX.DATA0] = ANALOG_INPUT 
        command[PACKET_INDEX.DATA1] = pin
        # 시리얼 송신
        ret = self.send(command)
        if self.__verbose:
            # print(f'[analogRead]: ', ret[5])
            pass
        val_5 = ret[RETURN_PACKET.DATA1]
        val_6 = ret[RETURN_PACKET.DATA2]
        return (val_6 <<8 | val_5)
    

class Servo:
    def __init__(self, verbose=True):
        self.__verbose = verbose
        self.__sender = None
        self.__pin = None
        self.__name = 'Servo'
        
    def attach(self, sender, pin):
        self.__sender = sender
        self.__pin = pin
        
    def move(self, val):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = SERVO 
        command[PACKET_INDEX.DATA0] = self.__pin 
        command[PACKET_INDEX.DATA1] = val
         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            # print(f'[Servo]: ', ret)
            pass
        return 1

    
class Ultrasonic:
    def __init__(self, verbose=False):
        self.__verbose = verbose
        self.__sender = None
        self.__trig = None
        self.__echo = None
        self.__name = 'Ultrasonic'
        
    def attach(self, sender, trig, echo):
        self.__sender = sender
        self.__echo = echo
        self.__trig = trig
        
    def distance(self):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = ULTRASONIC 
        command[PACKET_INDEX.DATA0] = self.__trig 
        command[PACKET_INDEX.DATA1] = self.__echo

         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            print(f'[Ultrasonic]: ', ret)
        return ret[RETURN_PACKET.DATA1]


class DCMotor:
    def __init__(self, verbose=False):
        self.__verbose = verbose
        self.__sender = None
        self.__pin_1 = None
        self.__pin_2 = None
        self.__name = 'DCMotor'
        
    def attach(self, sender, pin1, pin2):
        self.__sender = sender
        self.__pin_1 = pin1
        self.__pin_2 = pin2


    def go(self, val1, val2):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = DCMOTOR
        command[PACKET_INDEX.DATA0] = self.__pin_1 
        command[PACKET_INDEX.DATA1] = self.__pin_2
        command[PACKET_INDEX.DATA2] = val1
        command[PACKET_INDEX.DATA3] = val2


        # 시리얼 송신
        ret = self.__sender.send(command)
        
        if self.__verbose:
            print(f'[DCMOTOR] ', ret)

        return ret


class DHT11:
    def __init__(self, verbose=False):
        self.__verbose = verbose
        self.__sender = None
        self.__pin = None
        self.__name = 'DHT11'
        
    def attach(self, sender, pin):
        self.__sender = sender
        self.__pin = pin
        
    def read(self):
        command = NULL_COMMAND_PACKET[:]
        command[PACKET_INDEX.ACTION] = TMPHUM 
        command[PACKET_INDEX.DATA0] = self.__pin 

         # 시리얼 송신
        ret = self.__sender.send(command)
        if self.__verbose:
            print(f'[DHT11]: ', ret)

        tmp = ret[RETURN_PACKET.DATA1]
        hum = ret[RETURN_PACKET.DATA2]
        
        return tmp, hum


