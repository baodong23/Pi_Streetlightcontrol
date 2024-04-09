import data
import pyodbc
import time
from time import sleep
import sqlite3
import plcS7_1200
import connect_plcLogo
import updatedata
import MFM383_Max485
import mqtt_client
import serial
import RPi.GPIO as GPIO

def insertsqlserver(sql,val):
    con = pyodbc.connect(
    'DRIVER={freeTDS}; SERVER=45.119.83.12, 8183; DATABASE=AMT_ChieuSang_App; UID=webamt; PWD=@Amt$123456#; Trusted_Connection=no;TrustServerCertificate=yes;')
    mycursor= con.cursor()
    mycursor.execute(sql,val)
    con.commit()
    con.close()

def sqlitecn(dt):
    cnx = sqlite3.connect("/home/pi/bao/amtlight.db")
    mycursor = cnx.cursor()
    mycursor.execute(dt)
    data = mycursor.fetchone()
    cnx.close()
    return data

def S7getparatime1():
    time1 = [None]*4
    data = plcS7_1200.dbread_byte(1,0,4)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time1[0] = h_tr + ":" + s_tr 
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time1[1] = h_tr1 + ":" + s_tr1
    return time1
def S7getparatime2():
    time2 = [None]*4
    data = plcS7_1200.dbread_byte(1,12,4)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time2[0] = h_tr + ":" + s_tr 
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time2[1] = h_tr1 + ":" + s_tr1
    return time2
def S7getparatime3():
    time3 = [None]*4
    data = plcS7_1200.dbread_byte(1,24,4)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time3[0] = h_tr + ":" + s_tr 
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time3[1] = h_tr1 + ":" + s_tr1
    return time3
def S7getparatime4():
    time4 = [None]*4
    data = plcS7_1200.dbread_byte(1,36,4)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time4[0] = h_tr + ":" + s_tr 
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time4[1] = h_tr1 + ":" + s_tr1
    return time4
def S7time():
    timehome = [None]*2
    data = plcS7_1200.dbread_byte(1,240,4)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    timehome[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    timehome[1] = h_tr1 + ":" + s_tr1 + ":00"
    return timehome

def S7getcontroltime1_1():
    time1_1 = [None]*4
    data = plcS7_1200.dbread_byte(1,48,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time1_1[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time1_1[1] = h_tr1 + ":" + s_tr1 + ":00"
    time1_1[2] = data[4]
    time1_1[3] = data[5]
    return time1_1
def S7getcontroltime1_2():
    time1_2 = [None]*4
    data = plcS7_1200.dbread_byte(1,60,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time1_2[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time1_2[1] = h_tr1 + ":" + s_tr1 + ":00"
    time1_2[2] = data[4]
    time1_2[3] = data[5]
    return time1_2
def S7getcontroltime1_3():
    time1_3 = [None]*4
    data = plcS7_1200.dbread_byte(1,72,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr= str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time1_3[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time1_3[1] = h_tr1 + ":" + s_tr1 + ":00"
    time1_3[2] = data[4]
    time1_3[3] = data[5]
    #plcS7_1200.disconnect()
    return time1_3
def S7getcontroltime1_4():
    time1_4 = [None]*4
    data = plcS7_1200.dbread_byte(1,84,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time1_4[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time1_4[1] = h_tr1 + ":" + s_tr1 + ":00"
    time1_4[2] = data[4]
    time1_4[3] = data[5]
    #plcS7_1200.disconnect()
    return time1_4

def S7getcontroltime2_1():
    time2_1 = [None]*4
    #plcS7_1200.connect("192.168.8.173",0,1)
    data = plcS7_1200.dbread_byte(1,96,6)
    #print(data)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time2_1[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time2_1[1] = h_tr1 + ":" + s_tr1 + ":00"
    time2_1[2] = data[4]
    time2_1[3] = data[5]
    #plcS7_1200.disconnect()
    return time2_1
def S7getcontroltime2_2():
    time2_2 = [None]*4
    data = plcS7_1200.dbread_byte(1,108,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time2_2[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time2_2[1] = h_tr1 + ":" + s_tr1 + ":00"
    time2_2[2] = data[4]
    time2_2[3] = data[5]
    #plcS7_1200.disconnect()
    return time2_2
def S7getcontroltime2_3():
    time2_3 = [None]*4
    #plcS7_1200.connect("192.168.8.173",0,1)
    data = plcS7_1200.dbread_byte(1,120,6)
    #print(data)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time2_3[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time2_3[1] = h_tr1 + ":" + s_tr1 + ":00"
    time2_3[2] = data[4]
    time2_3[3] = data[5]
    #plcS7_1200.disconnect()
    return time2_3
def S7getcontroltime2_4():
    time2_4 = [None]*4
    #plcS7_1200.connect("192.168.8.173",0,1)
    data = plcS7_1200.dbread_byte(1,132,6)
    #print(data)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time2_4[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time2_4[1] = h_tr1 + ":" + s_tr1 + ":00"
    time2_4[2] = data[4]
    time2_4[3] = data[5]
    #plcS7_1200.disconnect()
    return time2_4

def S7getcontroltime3_1():
    time3_1 = [None]*4
    data = plcS7_1200.dbread_byte(1,144,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time3_1[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time3_1[1] = h_tr1 + ":" + s_tr1 + ":00"
    time3_1[2] = data[4]
    time3_1[3] = data[5]
    return time3_1
def S7getcontroltime3_2():
    time3_2 = [None]*4
    data = plcS7_1200.dbread_byte(1,156,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time3_2[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time3_2[1] = h_tr1 + ":" + s_tr1 + ":00"
    time3_2[2] = data[4]
    time3_2[3] = data[5]
    #plcS7_1200.disconnect()
    return time3_2
def S7getcontroltime3_3():
    time3_3 = [None]*4
    data = plcS7_1200.dbread_byte(1,168,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time3_3[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time3_3[1] = h_tr1 + ":" + s_tr1 + ":00"
    time3_3[2] = data[4]
    time3_3[3] = data[5]
    return time3_3
def S7getcontroltime3_4():
    time3_4 = [None]*4
    data = plcS7_1200.dbread_byte(1,180,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time3_4[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time3_4[1] = h_tr1 + ":" + s_tr1 + ":00"
    time3_4[2] = data[4]
    time3_4[3] = data[5]
    #plcS7_1200.disconnect()
    return time3_4

def S7getcontroltime4_1():
    time4_1 = [None]*4
    data = plcS7_1200.dbread_byte(1,192,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time4_1[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time4_1[1] = h_tr1 + ":" + s_tr1 + ":00"
    time4_1[2] = data[4]
    time4_1[3] = data[5]
    return time4_1
def S7getcontroltime4_2():
    time4_2 = [None]*4
    data = plcS7_1200.dbread_byte(1,204,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time4_2[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time4_2[1] = h_tr1 + ":" + s_tr1 + ":00"
    time4_2[2] = data[4]
    time4_2[3] = data[5]
    #plcS7_1200.disconnect()
    return time4_2
def S7getcontroltime4_3():
    time4_3 = [None]*4
    data = plcS7_1200.dbread_byte(1,216,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time4_3[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time4_3[1] = h_tr1 + ":" + s_tr1 + ":00"
    time4_3[2] = data[4]
    time4_3[3] = data[5]
    return time4_3
def S7getcontroltime4_4():
    time4_4 = [None]*4
    data = plcS7_1200.dbread_byte(1,228,6)
    h_tr = str(data[0]) if data[0]>=10 else "0"+str(data[0])
    s_tr=str(data[1]) if data[1]>=10 else "0"+str(data[1])
    time4_4[0] = h_tr + ":" + s_tr + ":00"
    h_tr1 = str(data[2]) if data[2]>=10 else "0"+str(data[2])
    s_tr1=str(data[3]) if data[3]>=10 else "0"+str(data[3])
    time4_4[1] = h_tr1 + ":" + s_tr1 + ":00"
    time4_4[2] = data[4]
    time4_4[3] = data[5]
    return time4_4

def Logogetcontroltime1():
    dt = connect_plcLogo.read_dataPLC("VW0")
    start1_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.starttime1_1 = start1_1

    dt = connect_plcLogo.read_dataPLC("VW2")
    stop1_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.stoptime1_1 = stop1_1

    dt = connect_plcLogo.read_dataPLC("VW4")
    start1_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.starttime1_2 = start1_2

    dt = connect_plcLogo.read_dataPLC("VW6")
    stop1_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.stoptime1_2 = stop1_2

    dt = connect_plcLogo.read_dataPLC("VW8")
    start1_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.starttime1_3 = start1_3

    dt = connect_plcLogo.read_dataPLC("VW10")
    stop1_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.stoptime1_3 = stop1_3

    dt = connect_plcLogo.read_dataPLC("VW12")
    start1_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.starttime1_4 = start1_4

    dt = connect_plcLogo.read_dataPLC("VW14")
    stop1_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol1.stoptime1_4 = stop1_4

    data.ontimeControl1(str(data.datasend.dttimecontrol1))
    #sql = "UPDATE time1 SET start1_1=?,stop1_1=?,u1_1=?,i1_1=?,start1_2=?,stop1_2=?,u1_2=?,i1_2=?,start1_3=?,stop1_3=?,u1_3=?,i1_3=?,start1_4=?,stop1_4=?,u1_4=?,i1_4=?"
    #val = (start1_1[:5],stop1_1[:5],0,0,start1_2[:5],stop1_2[:5],0,0,start1_3[:5],stop1_3[:5],0,0,start1_4[:5],stop1_4[:5],0,0)
    #updatedata.sqlupdate(sql,val)
def Logogetcontroltime2():
    dt = connect_plcLogo.read_dataPLC("VW16")
    start2_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.starttime2_1 = start2_1

    dt = connect_plcLogo.read_dataPLC("VW18")
    stop2_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.stoptime2_1 = stop2_1

    dt = connect_plcLogo.read_dataPLC("VW20")
    start2_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.starttime2_2 = start2_2

    dt = connect_plcLogo.read_dataPLC("VW22")
    stop2_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.stoptime2_2 = stop2_2

    dt = connect_plcLogo.read_dataPLC("VW24")
    start2_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.starttime2_3 = start2_3

    dt = connect_plcLogo.read_dataPLC("VW26")
    stop2_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.stoptime2_3 = stop2_3

    dt = connect_plcLogo.read_dataPLC("VW28")
    start2_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.starttime2_4 = start2_4

    dt = connect_plcLogo.read_dataPLC("VW30")
    stop2_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol2.stoptime2_4 = stop2_4

    data.ontimeControl2(str(data.datasend.dttimecontrol2))
    #sql = "UPDATE time2 SET start2_1=?,stop2_1=?,u2_1=?,i2_1=?,start2_2=?,stop2_2=?,u2_2=?,i2_2=?,start2_3=?,stop2_3=?,u2_3=?,i2_3=?,start2_4=?,stop2_4=?,u2_4=?,i2_4=?"
    #val = (start2_1[:5],stop2_1[:5],0,0,start2_2[:5],stop2_2[:5],0,0,start2_3[:5],stop2_3[:5],0,0,start2_4[:5],stop2_4[:5],0,0)
    #updatedata.sqlupdate(sql,val)
def Logogetcontroltime3():
    dt = connect_plcLogo.read_dataPLC("VW32")
    start3_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.starttime3_1 = start3_1

    dt = connect_plcLogo.read_dataPLC("VW34")
    stop3_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.stoptime3_1 = stop3_1

    dt = connect_plcLogo.read_dataPLC("VW36")
    start3_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.starttime3_2 = start3_2

    dt = connect_plcLogo.read_dataPLC("VW38")
    stop3_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.stoptime3_2 = stop3_2

    dt = connect_plcLogo.read_dataPLC("VW40")
    start3_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.starttime3_3 = start3_3

    dt = connect_plcLogo.read_dataPLC("VW42")
    stop3_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.stoptime3_3 = stop3_3

    dt = connect_plcLogo.read_dataPLC("VW44")
    start3_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.starttime3_4 = start3_4

    dt = connect_plcLogo.read_dataPLC("VW46")
    stop3_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol3.stoptime3_4 = stop3_4
    
    data.ontimeControl3(str(data.datasend.dttimecontrol3))
    #sql = "UPDATE time3 SET start3_1=?,stop3_1=?,u3_1=?,i3_1=?,start3_2=?,stop3_2=?,u3_2=?,i3_2=?,start3_3=?,stop3_3=?,u3_3=?,i3_3=?,start3_4=?,stop3_4=?,u3_4=?,i3_4=?"
    #val = (start3_1[:5],stop3_1[:5],0,0,start3_2[:5],stop3_2[:5],0,0,start3_3[:5],stop3_3[:5],0,0,start3_4[:5],stop3_4[:5],0,0)
    #updatedata.sqlupdate(sql,val)
def Logogetcontroltime4():
    dt = connect_plcLogo.read_dataPLC("VW48")
    start4_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.starttime4_1 = start4_1

    dt = connect_plcLogo.read_dataPLC("VW50")
    stop4_1 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.stoptime4_1 = stop4_1

    dt = connect_plcLogo.read_dataPLC("VW52")
    start4_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.starttime4_2 = start4_2

    dt = connect_plcLogo.read_dataPLC("VW54")
    stop4_2 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.stoptime4_2 = stop4_2

    dt = connect_plcLogo.read_dataPLC("VW56")
    start4_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.starttime4_3 = start4_3

    dt = connect_plcLogo.read_dataPLC("VW58")
    stop4_3 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.stoptime4_3 = stop4_3

    dt = connect_plcLogo.read_dataPLC("VW60")
    start4_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.starttime4_4 = start4_4

    dt = connect_plcLogo.read_dataPLC("VW62")
    stop4_4 = timehex_to_dec(dt)
    data.datasend.dttimecontrol4.stoptime4_4 = stop4_4

    data.ontimeControl4(str(data.datasend.dttimecontrol4))
    #sql = "UPDATE time4 SET start4_1=?,stop4_1=?,u4_1=?,i4_1=?,start4_2=?,stop4_2=?,u4_2=?,i4_2=?,start4_3=?,stop4_3=?,u4_3=?,i4_3=?,start4_4=?,stop4_4=?,u4_4=?,i4_4=?"
    #val = (start4_1[:5],stop4_1[:5],0,0,start4_2[:5],stop4_2[:5],0,0,start4_3[:5],stop4_3[:5],0,0,start4_4[:5],stop4_4[:5],0,0)
    #updatedata.sqlupdate(sql,val)
def timehex_to_dec(data):
    temp = 0
    for i in range(4):
        value = int(data)%16
        temp = temp + value*pow(10,i)
        data = int(data)/16
    hour = int(temp/100)
    minute = int(temp)%100
    h_tr = str(hour) if hour>=10 else "0"+str(hour)
    m_tr = str(minute) if minute>=10 else "0"+str(minute)
    s_tr = h_tr + ":" + m_tr + ":00"
    return s_tr

def light_status():
    light1 = int(plcS7_1200.mbread_bool(2,1,0,5))
    light2 = int(plcS7_1200.mbread_bool(2,1,0,6))
    light3 = int(plcS7_1200.mbread_bool(2,1,0,7))
    light4 = int(plcS7_1200.mbread_bool(3,1,0,0))

    data.datasend.dtlightstatus.light1 = light1
    data.datasend.dtlightstatus.light2 = light2
    data.datasend.dtlightstatus.light3 = light3
    data.datasend.dtlightstatus.light4 = light4

    data.onlightstatus(str(data.datasend.dtlightstatus))

def control_branch():
    controlload = sqlitecn("select * from status_control")
    data.datastatus.man1 = controlload[0]
    data.datastatus.man2 = controlload[1]
    data.datastatus.man3 = controlload[2]
    data.datastatus.man4 = controlload[3]
    data.datastatus.au1 = controlload[4]
    data.datastatus.au2 = controlload[5]
    data.datastatus.au3 = controlload[6]
    data.datastatus.au4 = controlload[7]
    data.sendstatus()
    data.onControl(str(data.datasend.dtstatus))

def savetimehome():
    t1 = [None]*2
    t1 = S7time()
    data.datasend.dttimehome.starttime = t1[0]
    data.datasend.dttimehome.stoptime = t1[1]
    
    sql = "UPDATE timehome SET start=?, stop=?"
    val = (t1[0][:5],t1[1][:5])
    updatedata.sqlupdate(sql,val)
    data.ontimehome(str(data.datasend.dttimehome))

def savetime1():
    t1 = [None]*4
    t1 = S7getcontroltime1_1()
    data.datasend.dttimecontrol1.starttime1_1 = t1[0]
    data.datasend.dttimecontrol1.stoptime1_1 = t1[1]
    data.datasend.dttimecontrol1.u1_1max = t1[2]
    data.datasend.dttimecontrol1.i1_1max = t1[3]

    t2 = [None]*4
    t2 = S7getcontroltime1_2()
    data.datasend.dttimecontrol1.starttime1_2 = t2[0]
    data.datasend.dttimecontrol1.stoptime1_2 = t2[1]
    data.datasend.dttimecontrol1.u1_2max = t2[2]
    data.datasend.dttimecontrol1.i1_2max = t2[3]

    t3 = [None]*4
    t3 = S7getcontroltime1_3()
    data.datasend.dttimecontrol1.starttime1_3 = t3[0]
    data.datasend.dttimecontrol1.stoptime1_3 = t3[1]
    data.datasend.dttimecontrol1.u1_3max = t3[2]
    data.datasend.dttimecontrol1.i1_3max = t3[3]

    t4 = [None]*4
    t4 = S7getcontroltime1_4()
    data.datasend.dttimecontrol1.starttime1_4 = t4[0]
    data.datasend.dttimecontrol1.stoptime1_4 = t4[1]
    data.datasend.dttimecontrol1.u1_4max = t4[2]
    data.datasend.dttimecontrol1.i1_4max = t4[3]

    sql = "UPDATE time1 SET start1_1=?,stop1_1=?,u1_1=?,i1_1=?,start1_2=?,stop1_2=?,u1_2=?,i1_2=?,start1_3=?,stop1_3=?,u1_3=?,i1_3=?,start1_4=?,stop1_4=?,u1_4=?,i1_4=?"
    val = (t1[0][:5],t1[1][:5],t1[2],t1[3],t2[0][:5],t2[1][:5],t2[2],t2[3],t3[0][:5],t3[1][:5],t3[2],t3[3],t4[0][:5],t4[1][:5],t4[2],t4[3])
    updatedata.sqlupdate(sql,val)
    data.ontimeControl1(str(data.datasend.dttimecontrol1))

def savetime2():
    t1 =[None]*4
    t1 = S7getcontroltime2_1()
    data.datasend.dttimecontrol2.starttime2_1 = t1[0]
    data.datasend.dttimecontrol2.stoptime2_1 = t1[1]
    data.datasend.dttimecontrol2.u2_1max = t1[2]
    data.datasend.dttimecontrol2.i2_1max = t1[3]

    t2 =[None]*4
    t2 = S7getcontroltime2_2()
    data.datasend.dttimecontrol2.starttime2_2 = t2[0]
    data.datasend.dttimecontrol2.stoptime2_2 = t2[1]
    data.datasend.dttimecontrol2.u2_2max = t2[2]
    data.datasend.dttimecontrol2.i2_2max = t2[3]

    t3 =[None]*4
    t3 = S7getcontroltime2_3()
    data.datasend.dttimecontrol2.starttime2_3 = t3[0]
    data.datasend.dttimecontrol2.stoptime2_3 = t3[1]
    data.datasend.dttimecontrol2.u2_3max = t3[2]
    data.datasend.dttimecontrol2.i2_3max = t3[3]

    t4 =[None]*4
    t4 = S7getcontroltime2_4()
    data.datasend.dttimecontrol2.starttime2_4 = t4[0]
    data.datasend.dttimecontrol2.stoptime2_4 = t4[1]
    data.datasend.dttimecontrol2.u2_4max = t4[2]
    data.datasend.dttimecontrol2.i2_4max = t4[3]

    sql = "UPDATE time2 SET start2_1=?,stop2_1=?,u2_1=?,i2_1=?,start2_2=?,stop2_2=?,u2_2=?,i2_2=?,start2_3=?,stop2_3=?,u2_3=?,i2_3=?,start2_4=?,stop2_4=?,u2_4=?,i2_4=?"
    val = (t1[0][:5],t1[1][:5],t1[2],t1[3],t2[0][:5],t2[1][:5],t2[2],t2[3],t3[0][:5],t3[1][:5],t3[2],t3[3],t4[0][:5],t4[1][:5],t4[2],t4[3])
    updatedata.sqlupdate(sql,val)
    data.ontimeControl2(str(data.datasend.dttimecontrol2))

def savetime3():
    t1 =[None]*4
    t1 = S7getcontroltime3_1()
    data.datasend.dttimecontrol3.starttime3_1 = t1[0]
    data.datasend.dttimecontrol3.stoptime3_1 = t1[1]
    data.datasend.dttimecontrol3.u3_1max = t1[2]
    data.datasend.dttimecontrol3.i3_1max = t1[3]

    t2 =[None]*4
    t2 = S7getcontroltime3_2()
    data.datasend.dttimecontrol3.starttime3_2 = t2[0]
    data.datasend.dttimecontrol3.stoptime3_2 = t2[1]
    data.datasend.dttimecontrol3.u3_2max = t2[2]
    data.datasend.dttimecontrol3.i3_2max = t2[3]

    t3 =[None]*4
    t3 = S7getcontroltime3_3()
    data.datasend.dttimecontrol3.starttime3_3 = t3[0]
    data.datasend.dttimecontrol3.stoptime3_3 = t3[1]
    data.datasend.dttimecontrol3.u3_3max = t3[2]
    data.datasend.dttimecontrol3.i3_3max = t3[3]

    t4 =[None]*4
    t4 = S7getcontroltime3_4()
    data.datasend.dttimecontrol3.starttime3_4 = t4[0]
    data.datasend.dttimecontrol3.stoptime3_4 = t4[1]
    data.datasend.dttimecontrol3.u3_4max = t4[2]
    data.datasend.dttimecontrol3.i3_4max = t4[3]

    sql = "UPDATE time3 SET start3_1=?,stop3_1=?,u3_1=?,i3_1=?,start3_2=?,stop3_2=?,u3_2=?,i3_2=?,start3_3=?,stop3_3=?,u3_3=?,i3_3=?,start3_4=?,stop3_4=?,u3_4=?,i3_4=?"
    val = (t1[0][:5],t1[1][:5],t1[2],t1[3],t2[0][:5],t2[1][:5],t2[2],t2[3],t3[0][:5],t3[1][:5],t3[2],t3[3],t4[0][:5],t4[1][:5],t4[2],t4[3])
    updatedata.sqlupdate(sql,val)
    data.ontimeControl3(str(data.datasend.dttimecontrol3))

def savetime4():
    t1 =[None]*4
    t1 = S7getcontroltime4_1()
    data.datasend.dttimecontrol4.starttime4_1 = t1[0]
    data.datasend.dttimecontrol4.stoptime4_1 = t1[1]
    data.datasend.dttimecontrol4.u4_1max = t1[2]
    data.datasend.dttimecontrol4.i4_1max = t1[3]

    t2 =[None]*4
    t2 = S7getcontroltime4_2()
    data.datasend.dttimecontrol4.starttime4_2 = t2[0]
    data.datasend.dttimecontrol4.stoptime4_2 = t2[1]
    data.datasend.dttimecontrol4.u4_2max = t2[2]
    data.datasend.dttimecontrol4.i4_2max = t2[3]

    t3 =[None]*4
    t3 = S7getcontroltime4_3()
    data.datasend.dttimecontrol4.starttime4_3 = t3[0]
    data.datasend.dttimecontrol4.stoptime4_3 = t3[1]
    data.datasend.dttimecontrol4.u4_3max = t3[2]
    data.datasend.dttimecontrol4.i4_3max = t3[3]

    t4 =[None]*4
    t4 = S7getcontroltime4_4()
    data.datasend.dttimecontrol4.starttime4_4 = t4[0]
    data.datasend.dttimecontrol4.stoptime4_4 = t4[1]
    data.datasend.dttimecontrol4.u4_4max = t4[2]
    data.datasend.dttimecontrol4.i4_4max = t4[3]

    sql = "UPDATE time4 SET start4_1=?,stop4_1=?,u4_1=?,i4_1=?,start4_2=?,stop4_2=?,u4_2=?,i4_2=?,start4_3=?,stop4_3=?,u4_3=?,i4_3=?,start4_4=?,stop4_4=?,u4_4=?,i4_4=?"
    val = (t1[0][:5],t1[1][:5],t1[2],t1[3],t2[0][:5],t2[1][:5],t2[2],t2[3],t3[0][:5],t3[1][:5],t3[2],t3[3],t4[0][:5],t4[1][:5],t4[2],t4[3])
    updatedata.sqlupdate(sql,val)
    data.ontimeControl4(str(data.datasend.dttimecontrol4))

def savecontrol():
    t1 =[None]*2
    t2 =[None]*2
    t3 =[None]*2
    t4 =[None]*2
    t1 = S7getparatime1()
    t2 = S7getparatime2()
    t3 = S7getparatime3()
    t4 = S7getparatime4()
    data.datasend.dttimecontrol.start1 = t1[0]
    data.datasend.dttimecontrol.stop1 = t1[1]
    data.datasend.dttimecontrol.start2 = t2[0]
    data.datasend.dttimecontrol.stop2 = t2[1]
    data.datasend.dttimecontrol.start3 = t3[0]
    data.datasend.dttimecontrol.stop3 = t3[1]
    data.datasend.dttimecontrol.start4 = t4[0]
    data.datasend.dttimecontrol.stop4 = t4[1]

    data.ontimeControl(str(data.datasend.dttimecontrol))


def error_code():
    par = [None]*32
    par = MFM383_Max485.read_fromMFM383A()
    if par == '':
        par = [0]*32
    setting = sqlitecn("SELECT * FROM settinghome")
    sql = "UPDATE status_control SET errorcode=?"
    if float(par[0]) > setting[0]:
        errorcode = "1"
    if float(par[1]) > setting[1]:
        errorcode = "2"
    if float(par[2]) > setting[2]:
        errorcode = "3"
    if float(par[8]) > setting[3]:
        errorcode = "4"
    if float(par[9]) > setting[4]:
        errorcode = "5"
    if float(par[10]) > setting[5]:
        errorcode = "6"
    if float(par[12]) > setting[6]:
        errorcode = "7"
    if float(par[13]) > setting[7]:
        errorcode = "8"
    if float(par[14]) > setting[8]:
        errorcode = "9"
    if float(par[27]) > setting[9]:
        errorcode = "10"
    if float(par[29]) > setting[11]:
        errorcode = "11"
    if errorcode != "0":
        time.sleep(0.1)
    else:
        errorcode = "0"
    updatedata.sqlupdate(sql , (errorcode, ))
    data.onerrorcode(errorcode)

def settinghome():
    setting = sqlitecn("SELECT * FROM settinghome")
    data.datasend.dtsettinghome.u1max = setting[0]
    data.datasend.dtsettinghome.u2max = setting[1]
    data.datasend.dtsettinghome.u3max = setting[2]
    data.datasend.dtsettinghome.i1max = setting[3]
    data.datasend.dtsettinghome.i2max = setting[4]
    data.datasend.dtsettinghome.i3max = setting[5]
    data.datasend.dtsettinghome.w1max = setting[6]
    data.datasend.dtsettinghome.w2max = setting[7]
    data.datasend.dtsettinghome.w3max = setting[8]
    data.datasend.dtsettinghome.Pfmax = setting[9]
    data.datasend.dtsettinghome.Irmax = setting[10]
    data.datasend.dtsettinghome.Qcmax = setting[11]

    data.onsettinghome(str(data.datasend.dtsettinghome))

def read_par():
    par = [None]*32
    par = MFM383_Max485.read_fromMFM383A()
    if par == '':
        data.datasend.dtpara.vol1 = 0
        data.datasend.dtpara.vol2 = 0
        data.datasend.dtpara.vol3 = 0
        data.datasend.dtpara.cur1 = 0
        data.datasend.dtpara.cur2 = 0
        data.datasend.dtpara.cur3 = 0
        data.datasend.dtpara.pow1 = 0
        data.datasend.dtpara.pow2 = 0
        data.datasend.dtpara.pow3 = 0
        data.datasend.dtpara.aPf = 0
        data.datasend.dtpara.Qc = 0
        data.datasend.dtpara.avol = 0
        data.datasend.dtpara.acur = 0
        data.datasend.dtpara.tpow = 0

        return [0]*32
    else:
        data.datasend.dtpara.vol1 = par[0]
        data.datasend.dtpara.vol2 = par[1]
        data.datasend.dtpara.vol3 = par[2]
        data.datasend.dtpara.cur1 = par[8]
        data.datasend.dtpara.cur2 = par[9]
        data.datasend.dtpara.cur3 = par[10]
        data.datasend.dtpara.pow1 = par[12]
        data.datasend.dtpara.pow2 = par[13]
        data.datasend.dtpara.pow3 = par[14]
        data.datasend.dtpara.aPf = par[27]
        data.datasend.dtpara.Qc = par[29]
        data.datasend.dtpara.avol = par[3]
        data.datasend.dtpara.acur = par[11]
        data.datasend.dtpara.tpow = par[21]

        return par

def data_mqtt():
    par = [None]*32
    controlload = sqlitecn("select * from status_control")
    time1 = sqlitecn("select * from time1")
    time2 = sqlitecn("select * from time2")
    time3 = sqlitecn("select * from time3")
    time4 = sqlitecn("select * from time4")
    timehome = sqlitecn("select * from timehome")
    par = MFM383_Max485.read_fromMFM383A()
    if par == '':
        par = [0]*32
    data = {"m1": controlload[0],"m2": controlload[1],
    "m3": controlload[2], "m4": controlload[3],
    "a1":controlload[4], "a2":controlload[5],
    "a3":controlload[6], "a4":controlload[7],
    "start1_1":time1[0], "stop1_1":time1[1],
    "u1_1":time1[2], "i1_1":time1[3],
    "start1_2":time1[4], "stop1_2":time1[5],
    "u1_2":time1[6], "i1_2":time1[7],
    "start1_3":time1[8], "stop1_3":time1[9],
    "u1_3":time1[10], "i1_3":time1[11],
    "start1_4":time1[12], "stop1_4":time1[13],
    "u1_4":time1[14], "i1_4":time1[15],
    "start2_1":time2[0], "stop2_1":time2[1],
    "u2_1":time2[2], "i2_1":time2[3],
    "start2_2":time2[4], "stop2_2":time2[5],
    "u2_2":time2[6], "i2_2":time2[7],
    "start2_3":time2[8], "stop2_3":time2[9],
    "u2_3":time2[10], "i2_3":time2[11],
    "start2_4":time2[12], "stop2_4":time2[13],
    "u2_4":time2[14], "i2_4":time2[15],
    "start3_1":time3[0], "stop3_1":time3[1],
    "u3_1":time3[2], "i3_1":time3[3],
    "start3_2":time3[4], "stop3_2":time3[5],
    "u3_2":time3[6], "i3_2":time3[7],
    "start3_3":time3[8], "stop3_3":time3[9],
    "u3_3":time3[10], "i3_3":time3[11],
    "start3_4":time3[12], "stop3_4":time3[13],
    "u3_4":time3[14], "i3_4":time3[15],
    "start4_1":time4[0], "stop4_1":time4[1],
    "u4_1":time4[2], "i4_1":time4[3],
    "start4_2":time4[4], "stop4_2":time4[5],
    "u4_2":time4[6], "i4_2":time4[7],
    "start4_3":time4[8], "stop4_3":time4[9],
    "u4_3":time4[10], "i4_3":time4[11],
    "start4_4":time4[12], "stop4_4":time4[13],
    "u4_4":time4[14],"i4_4":time4[15],
    "start":timehome[0], "stop":timehome[1],
    "Error_code":controlload[8],"Average_U": par[3],
    "Average_I": par[11], "Pf": par[27], 
    "Total_P": par[21], "Qc" : par[29]}

    return data

def readfrom_server(dt):
    option = sqlitecn("select option from cf")
    data.datastatus.server_control = 1
    if dt != '':
        if dt['m1'] == 1:
            data.manual1st(dt)
        elif dt['m1'] == 0:
            if dt['a1'] == 1:
                data.auto1st(dt)
            elif dt['a1'] == 0:
                data.manual1st(dt)
        if dt['m2'] == 1:
            data.manual2st(dt)
        elif dt['m2'] == 0:
            if dt['a2'] == 1:
                data.auto2st(dt)
            elif dt['a2'] == 0:
                data.manual2st(dt)
        if dt['m3'] == 1:
            data.manual3st(dt)
        elif dt['m3'] == 0:
            if dt['a3'] == 1:
                data.auto3st(dt)
            elif dt['a3'] == 0:
                data.manual3st(dt)
        if dt['m4'] == 1:
            data.manual4st(dt)
        elif dt['m4'] == 0:
            if dt['a4'] == 1:
                data.auto4st(dt)
            elif dt['a4'] == 0:
                data.manual4st(dt)
        sql = 'UPDATE status_control SET manual1=?,manual2=?,manual3=?,manual4=?,auto1=?,auto2=?,auto3=?,auto4=?'
        val = (dt['m1'],dt['m2'],dt['m3'],dt['m4'],dt['a1'],dt['a2'],dt['a3'],dt['a4'])
        updatedata.sqlupdate(sql,val)
        sql = 'UPDATE time1 SET start1_1=?,stop1_1=?,u1_1=?,i1_1=?,start1_2=?,stop1_2=?,u1_2=?,i1_2=?,start1_3 =?,stop1_3=?,u1_3=?,i1_3=?,start1_4=?,stop1_4=?,u1_4=?,i1_4=?'
        val = (dt['start1_1'],dt['stop1_1'],dt['u1_1'],dt['i1_1'],dt['start1_2'],dt['stop1_2'],dt['u1_2'],dt['i1_2'],
               dt['start1_3'],dt['stop1_3'],dt['u1_3'],dt['i1_3'],dt['start1_4'],dt['stop1_4'],dt['u1_4'],dt['i1_4'])
        updatedata.sqlupdate(sql,val)
        sql = 'UPDATE time2 SET start2_1=?,stop2_1=?,u2_1=?,i2_1=?,start2_2=?,stop2_2=?,u2_2=?,i2_2=?,start2_3 =?,stop2_3=?,u2_3=?,i2_3=?,start2_4=?,stop2_4=?,u2_4=?,i2_4=?'
        val = (dt['start2_1'],dt['stop2_1'],dt['u2_1'],dt['i2_1'],dt['start2_2'],dt['stop2_2'],dt['u2_2'],dt['i2_2'],
               dt['start2_3'],dt['stop2_3'],dt['u2_3'],dt['i2_3'],dt['start2_4'],dt['stop2_4'],dt['u2_4'],dt['i2_4'])
        updatedata.sqlupdate(sql,val)
        sql = 'UPDATE time3 SET start3_1=?,stop3_1=?,u3_1=?,i3_1=?,start3_2=?,stop3_2=?,u3_2=?,i3_2=?,start3_3 =?,stop3_3=?,u3_3=?,i3_3=?,start3_4=?,stop3_4=?,u3_4=?,i3_4=?'
        val = (dt['start3_1'],dt['stop3_1'],dt['u3_1'],dt['i3_1'],dt['start3_2'],dt['stop3_2'],dt['u3_2'],dt['i3_2'],
               dt['start3_3'],dt['stop3_3'],dt['u3_3'],dt['i3_3'],dt['start3_4'],dt['stop3_4'],dt['u3_4'],dt['i3_4'])
        updatedata.sqlupdate(sql,val)
        sql = 'UPDATE time4 SET start4_1=?,stop4_1=?,u4_1=?,i4_1=?,start4_2=?,stop4_2=?,u4_2=?,i4_2=?,start4_3 =?,stop4_3=?,u4_3=?,i4_3=?,start4_4=?,stop4_4=?,u4_4=?,i4_4=?'
        val = (dt['start4_1'],dt['stop4_1'],dt['u4_1'],dt['i4_1'],dt['start4_2'],dt['stop4_2'],dt['u4_2'],dt['i4_2'],
               dt['start4_3'],dt['stop4_3'],dt['u4_3'],dt['i4_3'],dt['start4_4'],dt['stop4_4'],dt['u4_4'],dt['i4_4'])
        updatedata.sqlupdate(sql,val)

        if option[0] == 1:
            data.shiftdt_S71200(1,48,int(int(dt['start1_1'][:2])))
            data.shiftdt_S71200(1,49,int(int(dt['start1_1'][3:5])))
            data.shiftdt_S71200(1,50,int(int(dt['stop1_1'][:2])))
            data.shiftdt_S71200(1,51,int(int(dt['stop1_1'][3:5])))
            data.shiftdt_S71200(1,60,int(int(dt['start1_2'][:2])))
            data.shiftdt_S71200(1,61,int(int(dt['start1_2'][3:5])))
            data.shiftdt_S71200(1,62,int(int(dt['stop1_2'][:2])))
            data.shiftdt_S71200(1,63,int(int(dt['stop1_2'][3:5])))
            data.shiftdt_S71200(1,72,int(int(dt['start1_3'][:2])))
            data.shiftdt_S71200(1,73,int(int(dt['start1_3'][3:5])))
            data.shiftdt_S71200(1,74,int(int(dt['stop1_3'][:2])))
            data.shiftdt_S71200(1,75,int(int(dt['stop1_3'][3:5])))
            data.shiftdt_S71200(1,84,int(int(dt['start1_4'][:2])))
            data.shiftdt_S71200(1,85,int(int(dt['start1_4'][3:5])))
            data.shiftdt_S71200(1,86,int(int(dt['stop1_4'][:2])))
            data.shiftdt_S71200(1,87,int(int(dt['stop1_4'][3:5])))
            data.shiftdt_S71200(1,96,int(int(dt['start2_1'][:2])))
            data.shiftdt_S71200(1,97,int(int(dt['start2_1'][3:5])))
            data.shiftdt_S71200(1,98,int(int(dt['stop2_1'][:2])))
            data.shiftdt_S71200(1,99,int(int(dt['stop2_1'][3:5])))
            data.shiftdt_S71200(1,108,int(int(dt['start2_2'][:2])))
            data.shiftdt_S71200(1,109,int(int(dt['start2_2'][3:5])))
            data.shiftdt_S71200(1,110,int(int(dt['stop2_2'][:2])))
            data.shiftdt_S71200(1,111,int(int(dt['stop2_2'][3:5])))
            data.shiftdt_S71200(1,120,int(int(dt['start2_3'][:2])))
            data.shiftdt_S71200(1,121,int(int(dt['start2_3'][3:5])))
            data.shiftdt_S71200(1,122,int(int(dt['stop2_3'][:2])))
            data.shiftdt_S71200(1,123,int(int(dt['stop2_3'][3:5])))
            data.shiftdt_S71200(1,132,int(int(dt['start2_4'][:2])))
            data.shiftdt_S71200(1,133,int(int(dt['start2_4'][3:5])))
            data.shiftdt_S71200(1,134,int(int(dt['stop1_4'][:2])))
            data.shiftdt_S71200(1,135,int(int(dt['stop1_4'][3:5])))
            data.shiftdt_S71200(1,144,int(int(dt['start3_1'][:2])))
            data.shiftdt_S71200(1,145,int(int(dt['start3_1'][3:5])))
            data.shiftdt_S71200(1,146,int(int(dt['stop3_1'][:2])))
            data.shiftdt_S71200(1,147,int(int(dt['stop3_1'][3:5])))
            data.shiftdt_S71200(1,156,int(int(dt['start3_2'][:2])))
            data.shiftdt_S71200(1,157,int(int(dt['start3_2'][3:5])))
            data.shiftdt_S71200(1,158,int(int(dt['stop3_2'][:2])))
            data.shiftdt_S71200(1,159,int(int(dt['stop3_2'][3:5])))
            data.shiftdt_S71200(1,168,int(int(dt['start3_3'][:2])))
            data.shiftdt_S71200(1,169,int(int(dt['start3_3'][3:5])))
            data.shiftdt_S71200(1,170,int(int(dt['stop3_3'][:2])))
            data.shiftdt_S71200(1,171,int(int(dt['stop3_3'][3:5])))
            data.shiftdt_S71200(1,180,int(int(dt['start3_4'][:2])))
            data.shiftdt_S71200(1,181,int(int(dt['start3_4'][3:5])))
            data.shiftdt_S71200(1,182,int(int(dt['stop3_4'][:2])))
            data.shiftdt_S71200(1,183,int(int(dt['stop3_4'][3:5])))
            data.shiftdt_S71200(1,192,int(int(dt['start4_1'][:2])))
            data.shiftdt_S71200(1,193,int(int(dt['start4_1'][3:5])))
            data.shiftdt_S71200(1,194,int(int(dt['stop4_1'][:2])))
            data.shiftdt_S71200(1,195,int(int(dt['stop4_1'][3:5])))
            data.shiftdt_S71200(1,204,int(int(dt['start4_2'][:2])))
            data.shiftdt_S71200(1,205,int(int(dt['start4_2'][3:5])))
            data.shiftdt_S71200(1,206,int(int(dt['stop4_2'][:2])))
            data.shiftdt_S71200(1,207,int(int(dt['stop4_2'][3:5])))
            data.shiftdt_S71200(1,216,int(int(dt['start4_3'][:2])))
            data.shiftdt_S71200(1,217,int(int(dt['start4_3'][3:5])))
            data.shiftdt_S71200(1,218,int(int(dt['stop4_3'][:2])))
            data.shiftdt_S71200(1,219,int(int(dt['stop4_3'][3:5])))
            data.shiftdt_S71200(1,228,int(int(dt['start4_4'][:2])))
            data.shiftdt_S71200(1,229,int(int(dt['start4_4'][3:5])))
            data.shiftdt_S71200(1,230,int(int(dt['stop4_4'][:2])))
            data.shiftdt_S71200(1,231,int(int(dt['stop4_4'][3:5])))
            data.shiftdt_S71200(1,240,int(int(dt['start'][:2])))
            data.shiftdt_S71200(1,241,int(int(dt['start'][3:5])))
            data.shiftdt_S71200(1,242,int(int(dt['stop'][:2])))
            data.shiftdt_S71200(1,243,int(int(dt['stop'][3:5])))
        elif option[0] == 2:
            if dt['a1'] == 1:
                data.shiftdt_Logo("VW0",int((str(dt['start1_1'])).replace(":","")))
                data.shiftdt_Logo("VW2",int((str(dt['stop1_1'])).replace(":","")))
                data.shiftdt_Logo("VW4",int((str(dt['start1_2'])).replace(":","")))
                data.shiftdt_Logo("VW6",int((str(dt['stop1_2'])).replace(":","")))
                data.shiftdt_Logo("VW8",int((str(dt['start1_3'])).replace(":","")))
                data.shiftdt_Logo("VW10",int((str(dt['stop1_3'])).replace(":","")))
                data.shiftdt_Logo("VW12",int((str(dt['start1_4'])).replace(":","")))
                data.shiftdt_Logo("VW14",int((str(dt['stop1_4'])).replace(":","")))
            if dt['a2'] == 1:
                data.shiftdt_Logo("VW16",int((str(dt['start2_1'])).replace(":","")))
                data.shiftdt_Logo("VW18",int((str(dt['stop2_1'])).replace(":","")))
                data.shiftdt_Logo("VW20",int((str(dt['start2_2'])).replace(":","")))
                data.shiftdt_Logo("VW22",int((str(dt['stop2_2'])).replace(":","")))
                data.shiftdt_Logo("VW24",int((str(dt['start2_3'])).replace(":","")))
                data.shiftdt_Logo("VW26",int((str(dt['stop2_3'])).replace(":","")))
                data.shiftdt_Logo("VW28",int((str(dt['start2_4'])).replace(":","")))
                data.shiftdt_Logo("VW30",int((str(dt['stop2_4'])).replace(":",""))) 
            if dt['a3'] == 1:
                data.shiftdt_Logo("VW32",int((str(dt['start3_1'])).replace(":","")))
                data.shiftdt_Logo("VW34",int((str(dt['stop3_1'])).replace(":","")))
                data.shiftdt_Logo("VW36",int((str(dt['start3_2'])).replace(":","")))
                data.shiftdt_Logo("VW38",int((str(dt['stop3_2'])).replace(":","")))
                data.shiftdt_Logo("VW40",int((str(dt['start3_3'])).replace(":","")))
                data.shiftdt_Logo("VW42",int((str(dt['stop3_3'])).replace(":","")))
                data.shiftdt_Logo("VW44",int((str(dt['start3_4'])).replace(":","")))
                data.shiftdt_Logo("VW46",int((str(dt['stop3_4'])).replace(":","")))
            if dt['a4'] == 1:
                data.shiftdt_Logo("VW48",int((str(dt['start4_1'])).replace(":","")))
                data.shiftdt_Logo("VW50",int((str(dt['stop4_1'])).replace(":","")))
                data.shiftdt_Logo("VW52",int((str(dt['start4_2'])).replace(":","")))
                data.shiftdt_Logo("VW54",int((str(dt['stop4_2'])).replace(":","")))
                data.shiftdt_Logo("VW56",int((str(dt['start4_3'])).replace(":","")))
                data.shiftdt_Logo("VW58",int((str(dt['stop4_3'])).replace(":","")))
                data.shiftdt_Logo("VW60",int((str(dt['start4_4'])).replace(":","")))
                data.shiftdt_Logo("VW62",int((str(dt['stop4_4'])).replace(":","")))
        dt = ''
        data.datastatus.server_control = 0
        print('successfull')
    else: 
        time.sleep(0.1)


def main():
    count = 0
    starttime = time.time()
    startdelay = time.time()
    temp = 0
    parameter = [None]*32
    id = updatedata.getsql('select ID from cf')
    mqtt_client.enable_sub("45.119.83.12",8883,"amt","123456","AmtLight/amt/Pub/"+str(id[0]))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while True:
        try:
            option = sqlitecn("select option, IP from cf")
            if data.datastatus.disconnectplc == 1:
                updatedata.updateoption(0,0)
                data.datastatus.disconnectplc = 0
                data.datasend.dtsystem.connect_PLC = 1
                data.onConnect_PLC(str(data.datasend.dtsystem))
            if data.datastatus.connectplc == 1 and option[0] == 1:
                if option[1] != '0' and option[1] != None:
                    if plcS7_1200.get_connected() == 1:
                        time.sleep(0.1)
                    else:
                        connect_plcLogo.disconnect()
                        data.datastatus.option_temp = option[1]
                        data.datastatus.connectplc = 0
                        plcS7_1200.connect(option[1],0,1)
                        data.datasend.dtsystem.connect_PLC = 1
            elif data.datastatus.connectplc == 1 and option[0] == 2:
                if option[1] != '0':
                    if connect_plcLogo.get_connected() == 1:
                        time.sleep(0.1)
                    else:
                        plcS7_1200.disconnect()
                        data.datastatus.option_temp = option[1]
                        data.datastatus.connectplc = 0
                        connect_plcLogo.connect(option[1],0x2000,0x1000)
                        data.datasend.dtsystem.connect_PLC = 1
            if option[0] == 1 and option[1] != data.datastatus.option_temp:
                if option[1] != '0' and option[1] != None:
                    connect_plcLogo.disconnect()
                    data.datastatus.option_temp = option[1]
                    data.datastatus.connectplc = 0
                    plcS7_1200.connect(option[1],0,1)
                    data.datasend.dtsystem.connect_PLC = 1
            elif option[0] == 2 and option[1] != data.datastatus.option_temp:
                if option[1] != '0':
                    plcS7_1200.disconnect()
                    data.datastatus.option_temp = option[1]
                    data.datastatus.connectplc = 0
                    connect_plcLogo.connect(option[1],0x2000,0x1000)
                    data.datasend.dtsystem.connect_PLC = 1
            parameter = read_par()
            mqtt_data = mqtt_client.readfrom_broker.receive()
            if temp == 1:
                if mqtt_data is not None:
                    readfrom_server(mqtt_data)
            else:
                temp = 1
            holddelay = time.time()
            endtime = time.time()
            if (holddelay - startdelay) >= 1:
                startdelay = time.time()
                dt = data_mqtt()
                mqtt_client.sendto_broker("45.119.83.12",8883,"amt","123456","AmtLight/amt/Sub/"+str(id[0]),dt)
            if (endtime - starttime) >= 60:
                count += 1
                starttime = time.time()
                updatedata.updateMFM383A(parameter)
                sql = "INSERT INTO MFM383A VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                val = (parameter[0],parameter[1],parameter[2],parameter[3],parameter[4],parameter[5],parameter[6],parameter[7],parameter[8],parameter[9],parameter[10],parameter[11],parameter[12],parameter[13],
                    parameter[14],parameter[15],parameter[16],parameter[17],parameter[18],parameter[19],parameter[20],parameter[21],parameter[22],parameter[23],parameter[24],parameter[25],
                    parameter[26],parameter[27],parameter[28],parameter[29],parameter[30],parameter[31])
                insertsqlserver(sql,val)
                print("60 giay")
            if count >= 172800:
                count = 0
                sql = "DELETE FROM MFM383A"
                updatedata.deletedata(sql)
            if data.datastatus.permission == 1 or data.datastatus.permission == 2:
                if data.datasend.dtsystem.connect_PLC == 1:
                    if plcS7_1200.get_connected() == 1 or connect_plcLogo.get_connected() == 1:
                        data.onConnect_PLC(str(data.datasend.dtsystem))
                        data.datasend.dtsystem.connect_PLC = 0
                if data.datamanage.fl_manage == 1:
                    manageload = sqlitecn("select * from cf")
                    data.datamanage.id = manageload[0]
                    data.datamanage.manage = manageload[1]
                    data.datamanage.branch = manageload[2]
                    data.sendmanage()
                    data.onManage(str(data.datasend.dtmanage))
                if option[0] == 1:
                    if data.datamanage.fl_time1 == 1:
                        data.datamanage.fl_time1 = 0
                        savetime1()
                    elif data.datamanage.fl_time2 == 1:
                        data.datamanage.fl_time2 = 0
                        savetime2()
                    elif data.datamanage.fl_time3 == 1:
                        data.datamanage.fl_time3 = 0
                        savetime3()
                    elif data.datamanage.fl_time4 == 1:
                        data.datamanage.fl_time4 = 0
                        savetime4()
                    elif data.datamanage.fl_time == 1:
                        data.datamanage.fl_time = 0
                        savetimehome()
                    elif data.datamanage.fl_manage == 1:
                        data.datamanage.fl_manage = 0
                        savecontrol()
                        light_status()
                    elif data.datamanage.fl_setting == 1:
                        data.datamanage.fl_setting = 0
                        settinghome()
                    elif data.datamanage.fl_system == 1:
                        data.datamanage.fl_system = 0
                        data.onloginok("1")
                elif option[0] == 2:
                    if data.datamanage.fl_time1 == 1:
                        data.datamanage.fl_time1 = 0
                        Logogetcontroltime1()
                    elif data.datamanage.fl_time2 == 1:
                        data.datamanage.fl_time2 = 0
                        Logogetcontroltime2()
                    elif data.datamanage.fl_time3 == 1:
                        data.datamanage.fl_time3 = 0
                        Logogetcontroltime3()
                    elif data.datamanage.fl_time4 == 1:
                        data.datamanage.fl_time4 = 0
                        Logogetcontroltime4()
                    elif data.datamanage.fl_manage == 1:
                         data.datamanage.fl_manage = 0
                    elif data.datamanage.fl_setting == 1:
                        data.datamanage.fl_setting = 0
                        settinghome()
                    elif data.datamanage.fl_system == 1:
                        data.datamanage.fl_system = 0
                        data.onloginok("1")
                    data.gettimelogo()               
                control_branch()
                error_code()
                data.onpara(str(data.datasend.dtpara))
            sleep(0.2)
        except Exception as error:
            print(error)
            option = sqlitecn("select option, IP from cf")
            if data.datastatus.disconnectplc == 1:
                updatedata.updateoption(0,0)
                data.datastatus.disconnectplc = 0
                data.datasend.dtsystem.connect_PLC = 1
                data.onConnect_PLC(str(data.datasend.dtsystem))
            '''if data.datastatus.connectplc == 1 and option[0] == 1:
                if option[1] != '0' and option[1] != None:
                    if plcS7_1200.get_connected() == 1:
                        time.sleep(0.1)
                    else:
                        connect_plcLogo.disconnect()
                        data.datastatus.option_temp = option[1]
                        plcS7_1200.connect(option[1],0,1)
                        data.datastatus.connectplc = 0
                        data.onConnect_PLC(str(data.datasend.dtsystem))
            elif data.datastatus.connectplc == 1 and option[0] == 2:
                if option[1] != '0':
                    if connect_plcLogo.get_connected() == 1:
                        time.sleep(0.1)
                    else:
                        plcS7_1200.disconnect()
                        data.datastatus.option_temp = option[1]
                        connect_plcLogo.connect(option[1],0x2000,0x1000)
                        data.datastatus.connectplc = 0
                        data.onConnect_PLC(str(data.datasend.dtsystem))'''
            data.onerror("1")
            data.datasend.dtsystem.connect_PLC = 0
            data.onConnect_PLC(str(data.datasend.dtsystem))
            plcS7_1200.disconnect()
            connect_plcLogo.disconnect()
