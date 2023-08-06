
MATRIX_LED = 0xC1
BUTTON     = 0xC2
BUZZER     = 0xC3
MPU_ACTION = 0xC4
DIGITAL    = 0xC5
ANALOG     = 0xC6
ULTRASONIC = 0xC7
SERVO      = 0xC8
TOUCH      = 0xC9
DCMOTOR    = 0xCA
TMPHUM      = 0xCB

# ----------------------------------------------------------------------
# MATRIX LED
# ----------------------------------------------------------------------
# LED 켜기 
DISPLAY_NUM = 0x01      # 0 ~ 9
DISPLAY_CHAR = 0x02     # A ~ Z
DISPLAY_SYMBOL = 0x03   # 0b11111, 0b00000, 0b00000, 0b00000, 0b11111, 
DISPLAY_COLOR = 0x04
DISPLAY_BRIGHT = 0x05
DISPLAY_XY =     0x06
DISPLAY_EFFECT = 0x07

BUZZER_BEEP = 0x01
BUZZER_MELODY = 0x02
BUZZER_NOTE = 0x03


DIGITAL_OUTPUT = 0x01
DIGITAL_INPUT = 0x02
DIGITAL_PULLUP = 0x03

ANALOG_OUTPUT = 0x01
ANALOG_INPUT = 0x02

class PinMode:
    OUTPUT = 0x01
    INPUT = 0x02
    INPUT_PULLUP = 0x03


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
P99_PIN = 99   # DUMMY PIN

RETURN_PACKET_LENGTH = 20

class Pin:
    P3 = 2    # ADC0    -> ANALOG IN 
    P0 = 10   # TOUCH1  -> ANALOG IN
    P4 = 9    #        -> ANALOG IN
    P5 = 40   # SW2     -> BUTTON A
    P6 = 41   # SW1     ->
    P7 = 39   # GPIO39  ->
    P1 = 4    # TOUCH3  -> ANALOG IN
    P8 = 38   # LED     ->
    P9 = 5    # ADC4    ->
    P10 = 6    # ADC3    -> ANALOG IN
    P11 = 7    # ADC2    -> BUTTON B
    P12 = 18   # GPIO 18 ->
    P2 = 8    # TOUCH2  -> ANALOG IN
    P13 = 12   # SCK     ->
    P14 = 13   # MISO    ->
    P15 = 11   # MOSI    ->
    P16 = 46   # GPIO46  ->
    P19 = 21   # SCL     -> SCL
    P20 = 14   # SDA     -> SDA
    P99 = 99   # DUMMY PIN
    

# 명령패킷의 인덱스
class PACKET_INDEX:
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

class Note:
    B0 =  0
    C1 =  1
    CS1 = 2
    D1 =  3
    DS1 = 4
    E1 =  5
    F1 =  6
    FS1 = 7
    G1 =  8
    GS1 = 9
    A1 =  10
    AS1 = 11
    B1 = 12
    C2 =  13
    CS2 = 14
    D2 =  15
    DS2 = 16
    E2 =  17
    F2 =  18
    FS2 = 19
    G2 =  20
    GS2 = 21
    A2 =  22
    AS2 = 23
    B2 =  24
    C3 =  25
    CS3 = 26
    D3 =  27
    DS3 = 28
    E3 =  29
    F3 =  30
    FS3 = 31
    G3  = 32
    GS3 = 33
    A3 = 34
    AS3 = 35
    B3  = 36
    C4  = 37
    CS4 = 38
    D4  = 39
    DS4 = 40
    E4  = 41
    F4  = 42
    FS4 = 43
    G4  = 44
    GS4  =45
    A4  = 46
    AS4  =47
    B4   =48
    C5   =49
    CS5  =50
    D5   =51
    DS5 = 52
    F5 =  53
    FS5 = 54
    G5 =  55
    GS5 = 56
    A5 =  57
    AS5 = 58
    B5 =  59
    C6 =  60
    CS6 = 61
    D6 =  62
    DS6 =  63
    E6  =  64
    F6  =  65
    G6  =  66
    GS6  = 67
    A6   = 68
    AS6  = 69
    B6   = 70
    C7   = 71
    CS7  = 72
    D7   = 73
    DS7  = 74
    E7   = 75
    F7   = 76
    FS7  = 77
    G7   = 78
    GS7  = 79
    A7   = 80
    AS7  = 81
    B7   = 82
    C8   = 83
    CS8  = 84
    DS8  = 85
    
    dict = {
        'B0':B0,    'C1':C1,    'CS1':CS1,   'D1':D1,    'DS1':DS1,   'E1':E1,    'F1':F1,    'FS1':FS1,   'G1':G1,    'GS1':GS1,
        'A1':A1,    'AS1':AS1,   'B1':B1,    'C2':C2,    'CS2':CS2,   'D2':D2,    'DS2':DS2,   'E2':E2,    'F2':F2,    'FS2':FS2,
        'G2':G2,    'GS2':GS2,   'A2':A2,    'AS2':AS2,   'B2':B2,    'C3':C3,    'CS3':CS3,   'D3':D3,    'DS3':DS3,   'E3':E3,
        'F3':F3,    'FS3':FS3,   'G3':G3,    'GS3':GS3,   'A3':A3,    'AS3':AS3,   'B3':B3,    'C4':C4,    'CS4':CS4,   'D4':D4,    
        'DS4':DS4,   'E4':E4,    'F4':F4,    'FS4':FS4,   'G4':G4,    'GS4':GS4,   'A4':A4,    'AS4':AS4,   'B4':B4,    'C5':C5,
        'CS5':CS5,   'D5':D5,    'DS5':DS5,  'F5':F5,    'FS5':FS5,   'G5':G5,    'GS5':GS5,   'A5':A5,    'AS5':AS5,   'B5':B5,
        'C6':C6,    'CS6':CS6,   'D6':D6,    'DS6':DS6,   'E6':E6,    'F6':F6,    'G6':G6,    'GS6':GS6 ,  'A6':A6,    'AS6':AS6,
        'B6':B6,    'C7':C7,    'CS7':CS7,   'D7':D7,    'DS7':DS7,   'E7':E7,    'F7':F7 ,   'FS7':FS7,   'G7':G7,    'GS7':GS7 ,
        'A7':A7,    'AS7':AS7,   'B7':B7,    'C8':C8,    'CS8':CS8,   'DS8':DS8 
}

    
class Symbol:
    CHAR_A = 'A'
    CHAR_B = 'B'
    CHAR_C = 'C'
    CHAR_D = 'D'
    CHAR_E = 'E'
    CHAR_F = 'F'
    CHAR_G = 'G'
    CHAR_H = 'H'
    CHAR_I = 'I'
    CHAR_J = 'J'
    CHAR_K = 'K'
    CHAR_L = 'L'
    CHAR_M = 'M'
    CHAR_N = 'N'
    CHAR_O = 'O'
    CHAR_P = 'P'
    CHAR_Q = 'Q'
    CHAR_R = 'R'
    CHAR_S = 'S'
    CHAR_T = 'T'
    CHAR_U = 'U'
    CHAR_V = 'V'
    CHAR_W = 'W'
    CHAR_X = 'X'
    CHAR_Y = 'Y'
    CHAR_ = 'Z'
    NUM_0 = '0'
    NUM_1 = '1'
    NUM_2 = '2'
    NUM_3 = '3'
    NUM_4 = '4'
    NUM_5 = '5'
    NUM_6 = '6'
    NUM_7 = '7'
    NUM_8 = '8'
    NUM_9 = '9'
    
    def __init__(self, symbol):
        self.value = symbol
        

class Color:
    #Primary Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    VIOLET = (181, 126, 220)
    ORANGE = (255, 165, 0)
    GREEN = (0, 128, 0)
    GRAY = (128, 128, 128)

    #Extended Colors
    IVORY = (255, 255, 240)
    BEIGE = (245, 245, 220)
    WHEAT = (245, 222, 179)
    TAN = (210, 180, 140)
    KHAKI = (195, 176, 145)
    SILVER = (192, 192, 192)
    CHARCOAL = (70, 70, 70)
    NAVYBLUE = (0, 0, 128)
    ROYALBLUE = (8, 76, 158)
    MEDIUMBLUE = (0, 0, 205)
    AZURE = (0, 127, 255)
    CYAN = (0, 255, 255)
    AQUAMARINE = (127, 255, 212)
    TEAL = (0, 128, 128)
    FORESTGREEN = (34, 139, 34)
    OLIVE = (128, 128, 0)
    LIME = (191, 255, 0)
    GOLD = (255, 215, 0)
    SALMON = (250, 128, 114)
    HOTPINK = (252, 15, 192)
    FUCHSIA = (255, 119, 255)
    PUCE = (204, 136, 153)
    PLUM = (132, 49, 121)
    INDIGO = (75, 0, 130)
    MAROON = (128, 0, 0)
    CRIMSON = (220, 20, 60)
    DEFAULT = (0, 0, 0)
    
    def __init__(self, color):
        self.value = color
        



# ----------------------------------------------------------------------
# PACKET
# ----------------------------------------------------------------------
#                      ff    55    len   idx   action DATA0  DATA1 DATA2 DATA3 DATA4 DATA5 DATA6 DATA7  DATA8  DATA9  DATA10  DATA11  DATA12  DATA13  END   
#                      FF    55    11    01    02     03     04    05    06    07    08    09    0A     0B     0C     0D      0E      0F      10      11
NULL_COMMAND_PACKET = [0xff, 0x55, 0x11, 0x00, 0x00,  0x00,  0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,  0x00,  0x00,  0x00,   0x00,   0x00,   0x00,   0x5a]
LENGTH_OF_PACKET = 20


