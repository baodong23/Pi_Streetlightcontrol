import logging
import snap7



logging.basicConfig(level=logging.INFO)

# Siemens LOGO devices Logo 8 is the default

Logo_8 = True

logger = logging.getLogger(__name__)

plc = snap7.logo.Logo()

def connect(ip, tsap_snap7, tsap_logo):
    plc.connect(ip, tsap_snap7, tsap_logo)

def disconnect():
    plc.disconnect()

# check connection between Logo and Gateway
def get_connected():
    if plc.get_connected():
        return 1
    else:
        return 0


def send_datatoPLC(address,dt):
    if plc.get_connected():
        plc.write(str(address),dt)
    else:
        logger.error("Conncetion failed")

def read_dataPLC(address):
    if plc.get_connected():
        data = plc.read(str(address))
        return data
    else: 
        logger.error("Connection failed")
