#https://www.blog.berrybase.de

import sys
import time
from ltp305 import LTP305

address = 0x61

if address not in [0x61, 0x62, 0x63]:
    raise ValueError("Invalid i2c address: 0x{:02x}. Run `i2c-detect -y 1` to discover breakouts.".format(address))


try:
    display = LTP305(address=address)
    display.clear()
    display.show()
except OSError:
    raise OSError("Unable to find LTP305 on i2c address: 0x{:02x}. Run `i2c-detect -y 1` to discover breakouts".format(address))


while True:

    display.set_character(0, "B")    #Show BE on the display
    display.set_character(5, "e")
    display.show()
    time.sleep(0.5)                  #Sleep 0.5 sec
    display.clear()

    ##############

    display.set_character(0, "e")    #ER
    display.set_character(5, "r")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "r")    #RR
    display.set_character(5, "r")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "r")    #RY
    display.set_character(5, "y")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "y")    #YB 
    display.set_character(5, "B")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "B")    #BA
    display.set_character(5, "a")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "a")    #AS
    display.set_character(5, "s")
    display.show()
    time.sleep(0.5)
    display.clear()

    ###############

    display.set_character(0, "s")    #SE
    display.set_character(5, "e")
    display.show()
    time.sleep(0.5)
    display.clear()

    ##############

    display.set_character(0, "e")    #E
    display.show()
    time.sleep(0.5)
    display.clear()

    
