import logging
import snap7
import time

logging.basicConfig(level=logging.INFO)

# Siemens S7-1200


logger = logging.getLogger(__name__)

plc = snap7.client.Client()

def connect(IP,rack,slot):
    #connect to PLC
    plc.connect(IP, rack, slot)

def disconnect():
    plc.disconnect()

def get_connected():
    if plc.get_connected():
        return 1
    else:
        return 0  

# write a bit to PLCS7_1200
def mbwrite_bool(start: int,size: int,place: int, data: bool) -> bool:     
    #write boolean to Merkers
    try:
        if plc.get_connected():
            reading = plc.mb_read(start, size)
            snap7.util.set_bool(reading, 0, place, data)
            plc.mb_write(start, size, reading)
        else:
            logger.error("Conncetion failed")
    except Exception as error:
        print(error)

#read a bit from PLCS7_1200
def mbread_bool(start: int, num_byte: int, byte_index: int, bool_index: bool) -> bool: 
    try:
        if plc.get_connected():
            reading = plc.mb_read(start, num_byte)
            data = snap7.util.get_bool(reading, byte_index, bool_index)    
            return data
        else:
            logger.error("Connection failed")
    except Exception as error:
        print(error)

#write a byte to PLCS7_1200
def dbwrite_byte(number, start, data):
    if plc.get_connected():
        plc.db_write(number, start, bytearray([data]))
    else:
        logger.error("Connection failed")

#read a byte from PLCS7_1200
def dbread_byte(number, start, amount):
    if plc.get_connected():
        data = plc.db_read(number, start, amount)
        return data
    else: 
        logger.error("Connection failed")
        return -1

#test 
def read_dataPLC():
    connect("192.168.8.173",0,1)
    while True:
        time1_1=[None]*6
        if plc.get_connected():
            #logger.info("connected")
            data = plc.mb_read(5, 1)
            print(data)
            #plcS7_1200.disconnect()
            time.sleep(1)
        else:
            logger.error("Conncetion failed")
