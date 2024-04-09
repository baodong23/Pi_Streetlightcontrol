import serial
import time
import struct
#import RPi.GPIO as GPIO

# Cấu hình kết nối serial
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Thay đổi cổng serial tương ứng
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Địa chỉ thiết bị Modbus
device_address = 2

def read_holding_registers(register_address, num_registers):
    # Xây dựng gói tin yêu cầu đọc holding registers
    request_packet = bytearray([device_address, 0x04, (register_address >> 8) & 0xFF, register_address & 0xFF, (num_registers >> 8) & 0xFF, num_registers & 0xFF])
    crc = calculate_crc(request_packet)
    #print(hex(crc))
    request_packet += crc.to_bytes(2, byteorder='little')
    
    # Gửi yêu cầu
    #print(request_packet)
    ser.write(request_packet)
    '''GPIO.output(18, 1)
    ser.write(request_packet)
    time.sleep(0.01)
    # Đọc phản hồi
    GPIO.output(18, 0)'''
    response = ser.read(5+2*num_registers)  # 5 bytes header + 2 bytes per register
    #print(response)
    # Xử lý phản hồi và trích xuất dữ liệu
    if len(response) == 5 + 2*num_registers:
        # Kiểm tra CRC
        response_packet = bytearray(response)
        if verify_crc(response_packet):
            data = response_packet[3:-2]
            registers = []
            for i in range(0, len(data), 2):
                registers.append((data[i] << 8) + data[i+1])
            return registers
    return None

def calculate_crc(packet):
    # Hàm tính giá trị CRC cho gói tin
    crc = 0xFFFF
    for byte in packet:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def verify_crc(packet):
    # Hàm kiểm tra giá trị CRC của gói tin
    crc = calculate_crc(packet[:-2])
    return crc.to_bytes(2, byteorder='little') == packet[-2:]

def read_fromMFM383A():

    # Đọc holding registers từ thiết bị Modbus
    registers = read_holding_registers(0, 64)
    if registers is not None:
        #print("Data: ", registers)
        value = []
        for i in range(0,64,2):
                temp = (registers[i]) | (registers[i+1]<<16)
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
        #print(value)
        return value
    else:
        print("Error: Không nhận được phản hồi hợp lệ")
        return ''