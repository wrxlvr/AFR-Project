import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#Functino to read SPI data from MCP3008 chip
#Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Function to convert data to voltage level,
#rounted to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

afr_channel = 0

delay = 1
times_looped = 0

while True:
    #Read AFR data from channel
    afr_level = ReadChannel(afr_channel)
    afr_volts = ConvertVolts(afr_level,2)

    #Print info
    print ("------------------------------")

    print("AFR: {} ({}V)".format(afr_level,afr_volts))
    print(times_looped)
    times_looped += 1

    #Wait before repeating loop
    time.sleep(delay)
