from machine import *
import utime


#____________this class ist not finished______________
#           LCD 1602 with pcf8574 expander

sda = Pin(0, Pin.OPEN_DRAIN)
scl = Pin(1, Pin.OUT)
#move address left
address = 0x27 << 1    
    
def delay():
    utime.sleep_ms(10)
    
def i2c_start():
    delay()
    sda.high()
    delay()
    scl.high()
    delay()
    sda.low()
    delay()
    scl.low()
    delay()

def i2c_stop():
    sda.low()
    delay()
    scl.high()
    delay()
    sda.high()
    delay()
    scl.low()
    delay()
    scl.high()
    
def send_byte(byte):
    for i in range(8,0,-1):
        if byte & 0x80 > 0:
            sda.high()
        else:
            sda.low()
        delay()
        scl.high()
        delay()
        scl.low()
        byte <<= 1
    delay()
    sda.high()
    delay()
    #wait for ack
    while sda.value() == 1:
        pass
    
    scl.high()
    delay()
    scl.low()
    
    return True

#Register Select = P0
#Read Write = P1
#Enable = P2
#Backlight = P3
BACK_LIGHT = 1<<3   
#exmaple char
heartChar = [
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000,
  0b00000
]

#basic i2c communication
i2c_start()
send_byte(address)
#turn backlight on
send_byte(BACK_LIGHT) 
i2c_stop()
