# -*-coding:utf-8-*-
import sys
import serial
import time

P3_PIN = 2    # ADC0    -> ANALOG IN 
P0_PIN = 10   # TOUCH1  -> ANALOG IN
P4_PIN = 9    #        -> ANALOG IN
P5_PIN = 40   # SW2     -> BUTTON A
P6_PIN = 41   # SW1     ->
P7_PIN = 39   # GPIO39  ->
P1_PIN = 4    # TOUCH3  -> ANALOG IN
P8_PIN = 38   # LED     ->
P9_PIN = 5    # ADC4    ->
P10_PIN = 6    # ADC3    -> ANALOG IN
P11_PIN = 7    # ADC2    -> BUTTON B
P12_PIN = 18   # GPIO 18 ->
P2_PIN = 8    # TOUCH2  -> ANALOG IN
P13_PIN = 12   # SCK     ->
P14_PIN = 13   # MISO    ->
P15_PIN = 11   # MOSI    ->
P16_PIN = 46   # GPIO46  ->
P19_PIN = 21   # SCL     -> SCL
P20_PIN = 14   # SDA     -> SDA

RETURN_PACKET_LENGTH = 20

# 명령타입
class CommandType:
    FORCE_STOP = 0x01
    MOVE_FORWARD_BLOCK = 0x02
    MOVE_BACKWARD_BLOCK = 0x03
    TURN_LEFT_BLOCK = 0x04
    TURN_RIGHT_BLOCK = 0x05
    TURN_BACK_BLOCK = 0x06
    MOVE_FORWARD_LINE = 0x07
    TURN_LEFT_LINE = 0x08
    TURN_RIGHT_LINE = 0x09
    TURN_BACK_LINE = 0x0A
    SET_MOVE_SPEED = 0x0B
    MOVE_FORWARD_SPEED = 0x0C
    MOVE_LEFT_SPEED = 0x0D
    MOVE_RIGHT_SPEED = 0x0E
    MOVE_BACKWARD_SPEED = 0x10
    MOVE_FORWARD_LRSPEED = 0x11
    MOVE_BACKWARD_LRSPEED = 0x12
    MOVE_UNIT = 0x13
    SPIN_DEGREE = 0x14
    WHEEL_SET_SPEED = 0x15
    WHEEL_RUN = 0x16
    WHEEL_RUN_UNIT = 0x17
    WHEEL_RUN_LRUNIT = 0x18
    TOPMOTOR_SET_SPEED = 0x19
    TOPMOTOR_TURN = 0x1A
    TOPMOTOR_TURN_UNIT = 0x1B
    TOPMOTOR_MOVE_ABSOLUTE = 0x1C
    TOPMOTOR_STOP = 0x1D
    LED_TURN = 0x1E
    DRAW_SHAPE = 0x20
    DRAW_CIRCLE = 0x21
    DRAW_SEMICIRCLE = 0x22
    DRAW_SEMICIRCEL_UNIT = 0x23
    MELODY_BEEP = 0x24
    MELODY_MUTE = 0x25
    MELODY_SET_BMP = 0x26
    MELODY_PLAY_FREQ = 0x27
    SENSOR_GET_COLOR = 0x28
    SENSOR_GET_OBJECT = 0x29
    SENSOR_GET_LINE = 0x2A
    TOGGLE_LINERRACER = 0x2B
    BOTPI_STOP = 0x2C
    BOTPI_EMERGENCY_STOP = 0x2D
    BOTPI_INITIALIZE = 0x2E
    BOTPI_RESET = 0x30
    BOTPI_CLEAR = 0x31


# 명령패킷의 인덱스
class PacketIndex:
    START_1 = 0
    START_2 = 1
    LENGTH = 2
    INDEX = 3
    ACTION = 4
    DATA0 = 5
    DATA1 = 6
    DATA2 = 7
    DATA3 = 8
    DATA4 = 9
    DATA5 = 10
    DATA6 = 11
    DATA7 = 12
    DATA8 = 13
    DATA9 = 14
    DATA10 = 15
    DATA11 = 16
    DATA12 = 17
    DATA13 = 18
    END = 19


# 리턴 패킷의 인덱스
class RETURN_PACKET:
    HEADER_1 = 0
    HEADER_2 = 1
    INDEX = 2
    LENGTH = 3
    DATA0 = 4
    DATA1 = 5
    DATA2 = 6
    DATA3 = 7
    DATA4 = 8
    DATA5 = 9
    DATA6 = 10
    DATA7 = 11
    DATA8 = 12
    DATA9 = 13
    DATA10 = 14
    DATA11 = 15
    DATA12 = 16
    DATA13 = 17
    DATA14 = 18
    END = 19


class ModeType:
    MAPBOARD = 0x01
    CONTROL = 0x02
    RGB = 0x3
    TOP_STEPPER = 0x04
    OBJECT_DETECTER = 0x05
    LINE_DETECTOR = 0x06
    COLOR_DETECTOR = 0x7
    BATTERY = 0x08
    VERSION = 0x9
    REALTIME = 0x0A
    DRAWSHAPE = 0x0B
    PRECISION_CTR = 0x0C
    MELODY = 0x0D
    LINEMAP = 0x0E
    RESET = 0x0F
    EMERGENCY_STOP = 0x11
    LINE = 0x12
    INITIALIZE = 0x22
    MOTOR_SPEED = 0x33


# Command Type
COMMANDTYPE_WRITE = 0x01
COMMANDTYPE_READ = 0x02
COMMANDTYPE_RETURN = 0x03

# 디바이스 타입
HWTYPE_BOTPI = 0x00
HWTYPE_XBLOCK = 0x10

# LED 색상 YELLOW
TEST_COMMAND = [
    0xff, 0x55, 0x07, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x5a
]

# ff 55 len idx action DATA0 DATA1 DATA2 DATA3 END   
# FF 55 07  01  02     03    04    05    06    5A
NULL_COMMAND_PACKET = [
    0xff, 0x55, 0x07, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x5a
]

DEFAULT_MOTOR_SPEED = 0x96      # 150


LED = {
    "off": [0, 0, 0],
    "red": [255, 0, 0],
    "orange": [255, 165, 0],
    "yellow": [255, 255, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "skyblue": [0, 255, 255],
    "purple": [139, 0, 255],
    "white": [255, 255, 255],
}

LED_COLOR = [
    LED["off"], LED["red"], LED["orange"], LED["yellow"], LED["green"],
    LED["blue"], LED["skyblue"], LED["purple"], LED["white"]
]


class LedColor:
    OFF = LED["off"]
    RED = LED["red"]
    ORANGE = LED["orange"]
    YELLOW = LED["yellow"]
    GREEN = LED["green"]
    BLUE = LED["blue"]
    SKYBLUE = LED["skyblue"]
    PURPLE = LED["purple"]
    WHITE = LED["white"]


class BBMiniBoard:

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
            print("KamibotPi close(): Calling sys.exit(0): Hope to see you soon!")
        sys.exit(0)

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
            print(data)
            print('return data length {0}'.format(len(data)))

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


    def send(self, command):
        if self.__verbose:
            print("\n *** sendCommand ***")

        # command = NULL_COMMAND_PACKET[:]
        # command[PacketIndex.INDEX] = self.__get_idx()
        # command[PacketIndex.ACTION] = 0x02

        command[PacketIndex.INDEX] = self.__get_idx()
        print(command);
        
        try:
            self.sr.write(bytes(bytearray(command)))
            self.sr.flush()
        except Exception as e:
            print('An Exception occurred!', e)
            return []
        # self.__process_return()
        return self.__process_return()

    
