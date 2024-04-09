import plcS7_1200

plcS7_1200.connect("192.168.8.173", 0, 1)
light = [None]*4
light[0] = int(plcS7_1200.mbread_bool(2,1,0,5))
light[1] = int(plcS7_1200.mbread_bool(2,1,0,6))
light[2] = int(plcS7_1200.mbread_bool(2,1,0,7))
light[3] = int(plcS7_1200.mbread_bool(3,1,0,0))

print(light)
