import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import spidev
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts



afr_channel = 0


while True:
    afr_level = mcp.read_adc(afr_channel)
    afr_volts = ConvertVolts(afr_level,2)

        #Print info
    print ("------------------------------")

    print("AFR: {} ({}V)".format(afr_level,afr_volts))
    print(times_looped)
    times_looped += 1

    #Wait before repeating loop
    time.sleep(delay)
