from pymodbus.client import ModbusSerialClient
import struct

client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0', 
    baudrate=9600,
    stopbit=1,
    timeout=1
)

def read_fromMFM383A(register_address, quantity, address):
    if client.connect():
        try:
            response = client.read_input_registers(register_address, quantity, address)
            data = response.registers
            value = []
            count = 0
            for i in range(32):
                temp = (data[count]) | (data[count+1]<<16)
                if temp != 0:
                    if len(str(hex(temp)).replace("0x","")) == 4:
                        hex_str = str(hex(temp)).replace("0x","") + "0000"
                    elif len(str(hex(temp)).replace("0x","")) == 3:
                        hex_str = "0" + str(hex(temp)).replace("0x","") + "0000"
                    elif len(str(hex(temp)).replace("0x","")) == 2:
                        hex_str = "00" + str(hex(temp)).replace("0x","") + "0000"
                    elif len(str(hex(temp)).replace("0x","")) == 1:
                        hex_str = "000" + str(hex(temp)).replace("0x","") + "0000"
                    elif len(str(hex(temp)).replace("0x","")) == 5:
                        hex_str = str(hex(temp)).replace("0x","") + "000"
                    elif len(str(hex(temp)).replace("0x","")) == 6:
                        hex_str = str(hex(temp)).replace("0x","") + "00"
                    elif len(str(hex(temp)).replace("0x","")) == 7:
                        hex_str = str(hex(temp)).replace("0x","") + "0"
                    elif len(str(hex(temp)).replace("0x","")) == 8:
                        hex_str = str(hex(temp)).replace("0x","")
                    float_bytes = bytes.fromhex(hex_str)  # Chuyển đổi hex string thành bytes
                    float_num = struct.unpack('!f', float_bytes)[0]
                    value.append("{:.2f}".format(float_num))
                else:
                    value.append(temp)
                count = count+2
            if response.isError():
                print("Error data")
                return 'Error'
            else:
                print(value)
                return value
        except:
            pass
        finally:
            client.close()
    else:
        print("Can't connect to MFM383A")


if __name__ == '__main__':
    read_fromMFM383A(0x0000, 64, 2)