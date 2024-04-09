from web import socketio, request, session
from datetime import datetime
import handle
import json
import model
import updatedata
import lightcontrol
import connect_plcLogo
import time
import plcS7_1200
import setip

class datasend():
    dtmanage = model.js_manage()
    dtbranch = model.js_btnbranch()
    dtstatus = model.js_status()
    dttimecontrol1 = model.js_timecontrol1()
    dttimecontrol2 = model.js_timecontrol2()
    dttimecontrol3 = model.js_timecontrol3()
    dttimecontrol4 = model.js_timecontrol4()
    dtpara = model.js_MFMpara()
    dtsystem = model.js_system()
    dtlogin = model.js_login()
    dttimehome = model.js_timehome()
    dttimecontrol = model.js_timecontrol()
    dtsettinghome = model.js_settinghome()
    dtlightstatus = model.js_lightstatus()
    temp = 0
    m = lightcontrol.main
    
class datamanage():
    fl_manage = 0
    fl_time1 = 0
    fl_time2 = 0
    fl_time3 = 0
    fl_time4 = 0
    fl_time = 0
    fl_setting = 0
    fl_system = 0
    id = 0
    manage = 0
    branch = 0

class datastatus():
    man1 = 0
    man2 = 0
    man3 = 0 
    man4 = 0
    au1 = 0
    au2 = 0
    au3 = 0
    au4 = 0
    option_temp = '0'
    server_control = 0
    permission = 0
    ip_address = 0
    error = 0
    connectplc = 0
    disconnectplc = 0
    count4 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    manual1 = 0
    manual2 = 0
    manual3 = 0
    manual4 = 0

def start():
    t = socketio.start_background_task(target=datasend.m)
    socketio.sleep(1)
    print('reading all data...')

def onManage(msg):
    handle.onManage(msg)

def onControl(msg):
    handle.onControl(msg)

def ontimeControl1(msg):
    handle.ontimeControl1(msg)
def ontimeControl2(msg):
    handle.ontimeControl2(msg)
def ontimeControl3(msg):
    handle.ontimeControl3(msg)
def ontimeControl4(msg):
    handle.ontimeControl4(msg)
def ontimeControl(msg):
    handle.ontimeControl(msg)
def ontimehome(msg):
    handle.ontimehome(msg)
#send MFM383 parameter to web 
def onpara(msg):
    handle.onpara(msg)
def onip(msg):
    handle.onip(msg)
#send error to web when error occur
def onerror(msg):
    handle.onerror(msg)
def onerrorcode(msg):
    handle.onerrorcode(msg)
def onConnect_PLC(msg):
    handle.onConnect_PLC(msg)
def onlogin(msg):
    handle.onlogin(msg)
def onsettinghome(msg):
    handle.onsettinghome(msg)
def onsuccess(msg):
    handle.onsuccess(msg)
def onlightstatus(msg):
    handle.onlightstatus(msg)
def onloginok(msg):
    handle.onloginok(msg)
def sendmanage():
    datasend.dtmanage.jsid = datamanage.id
    datasend.dtmanage.jsmanager = datamanage.manage
    datasend.dtmanage.jslightbranch = datamanage.branch

def sendstatus():
    datasend.dtstatus.jsmanual1 = datastatus.man1
    datasend.dtstatus.jsmanual2 = datastatus.man2
    datasend.dtstatus.jsmanual3 = datastatus.man3
    datasend.dtstatus.jsmanual4 = datastatus.man4
    datasend.dtstatus.jsauto1 = datastatus.au1
    datasend.dtstatus.jsauto2 = datastatus.au2
    datasend.dtstatus.jsauto3 = datastatus.au3
    datasend.dtstatus.jsauto4 = datastatus.au4

def parsejson(js):
    dta = json.loads(js)
    return dta

def handle_msg(msg):
    dta = parsejson(msg)
    a = dta['cmd']
    datastatus.ip_address = request.remote_addr
    print('ip address:', datastatus.ip_address)
    datauser = updatedata.getsql("SELECT * FROM datauser")
    onip(str(datauser[0]))
    if (a == 'manage'):
        manage(dta['data'])
    elif (a == 'refresh'):
        refresh(dta['data'])
        print('refresh')
    elif (a == 'option'):
        datastatus.option_temp = '0'
        if dta['data'][1] != '':
            updatedata.updateoption(dta['data'][0], dta['data'][1])
        if dta['data'][2] != '':
            setip.IPconfig(dta['data'][2],dta['data'][3],dta['data'][4])
    elif (a == 'login'):
        print(dta['data'])
        checkLogin(dta['data'])
    elif (a == 'logout'):
        checklogout()
    elif (a == 'm1'):
        manual1st(dta['data'])
    elif (a == 'm2'):
        manual2st(dta['data'])
    elif (a == 'm3'):
        manual3st(dta['data'])
    elif (a == 'm4'):
        manual4st(dta['data'])
    elif (a == 'a1'):
        auto1st(dta['data'])
    elif (a == 'a2'):
        auto2st(dta['data'])
    elif (a == 'a3'):
        auto3st(dta['data'])
    elif (a == 'a4'):
        auto4st(dta['data'])
    elif (a == 'ui1-max'):
        print(dta['data'])
        ui1_max(dta['data'])
    elif (a == 'ui2-max'):
        ui2_max(dta['data'])
    elif (a == 'ui3-max'):
        ui3_max(dta['data'])
    elif (a == 'ui4-max'):
        ui4_max(dta['data'])
    elif (a == 'settime-home'):
        s = str(dta['data'][1])
        s = s.replace(":","")
        timehome(dta['data'][0],s,dta['data'][1])
    elif (a == 'settinghome'):
        print(dta['data'])
        settinghome(dta['data'])
    elif (a == 'settingbranch1'):
        s = str(dta['data'][1])
        s = s.replace(":","")
        branch1time(dta['data'][0],s,dta['data'][1])
    elif (a == 'settingbranch2'):
        s = str(dta['data'][1])
        s = s.replace(":","")
        branch2time(dta['data'][0],s,dta['data'][1])
    elif (a == 'settingbranch3'):
        s = str(dta['data'][1])
        s = s.replace(":","")
        branch3time(dta['data'][0],s,dta['data'][1])
    elif (a == 'settingbranch4'):
        s = str(dta['data'][1])
        s = s.replace(":","")
        branch4time(dta['data'][0],s,dta['data'][1])
    elif (a == 'set-datetime'):
        print(dta['data'])
        setdatetime(dta['data'])
    elif (a == 'delete'):
        delete(dta['data'])
    elif (a == 'copy1'):
        copy1(dta['data'])
    elif (a == 'copy2'):
        copy2(dta['data'])
    elif (a == 'copy3'):
        copy3(dta['data'])
    elif (a == 'copy4'):
        copy4(dta['data'])
    elif (a == 'plc'):
        print(1)
        datastatus.disconnectplc = 1
    elif (a == 'replc'):
        print(1)
        datastatus.connectplc = 1

def checkLogin(dt):
    check = updatedata.getsql("select * from systemlogin")
    if (int(dt['user']) == 1 and int(dt['pass']) == check[1]):
        datastatus.permission = 1
        ip_address = request.remote_addr
        datasend.dtlogin.login = ip_address
        datasend.dtsystem.connect_PLC = 1
        onlogin(str(datasend.dtlogin))
        updatedata.updatedatauser(ip_address, datastatus.permission)
        print('ip address:', ip_address)
    elif (int(dt['user']) == 2 and int(dt['pass']) == check[3]):
        datastatus.permission = 2
        ip_address = request.remote_addr
        datasend.dtlogin.login = ip_address
        datasend.dtsystem.connect_PLC = 1
        onlogin(str(datasend.dtlogin))
        updatedata.updatedatauser(ip_address, datastatus.permission)
        print('ip address:', ip_address)

def checklogout():
    ip_address = request.remote_addr
    check = updatedata.getsql("select IP_client from datauser")
    if ip_address == check[0]:
        datastatus.permission = 0
        updatedata.updatedatauser(0,0)

def checkoption():
    check = updatedata.getsql("select option from cf")
    return check[0]

def settinghome(dt):
    if dt[0] == "U1max":
        sql = "UPDATE settinghome SET U1max=?"
    elif dt[0] == "U2max":
        sql = "UPDATE settinghome SET U2max=?"
    elif dt[0] == "U3max":
        sql = "UPDATE settinghome SET U3max=?"
    elif dt[0] == "I1max":
        sql = "UPDATE settinghome SET I1max=?"
    elif dt[0] == "I2max":
        sql = "UPDATE settinghome SET I2max=?"
    elif dt[0] == "I3max":
        sql = "UPDATE settinghome SET I3max=?"
    elif dt[0] == "W1max":
        sql = "UPDATE settinghome SET W1max=?"
    elif dt[0] == "W2max":
        sql = "UPDATE settinghome SET W2max=?"
    elif dt[0] == "W3max":
        sql = "UPDATE settinghome SET W3max=?"
    elif dt[0] == "Pfmax":
        sql = "UPDATE settinghome SET Pfmax=?"
    elif dt[0] == "Irmax":
        sql = "UPDATE settinghome SET Irmax=?"
    elif dt[0] == "Qcmax":
        sql = "UPDATE settinghome SET Qcmax=?"
    updatedata.sqlupdate(sql,(dt[1],))

def timehome(dt,s_tr,dt1):
    option = checkoption()
    if (datastatus.permission == 1) or datastatus.server_control == 1:
        if dt == 'start':
            if (option == 1):
                hour = int(int(s_tr) / 100)
                shiftdt_S71200(1,240,hour)
                minute  = int(int(s_tr) % 100)
                shiftdt_S71200(1,241,minute)
                updatedata.sqlupdate("UPDATE timehome SET start=?",(dt1,))
        elif dt == 'stop':
            if (option == 1):
                hour = int(int(s_tr) / 100)
                shiftdt_S71200(1,242,hour)
                minute  = int(int(s_tr) % 100)
                shiftdt_S71200(1,243,minute)
                updatedata.sqlupdate("UPDATE timehome SET stop=?",(dt1,))

def gettimelogo():
    logo_branch1()
    logo_branch2()
    logo_branch3()
    logo_branch4()
    ontimeControl(str(datasend.dttimecontrol))
    onlightstatus(str(datasend.dtlightstatus))

def logo_branch1():
    def gettime(start, stop, light):
        datasend.dttimecontrol.start1 = start
        datasend.dttimecontrol.stop1 = stop
        datasend.dtlightstatus.light1 = light

    if (datastatus.permission == 1):
        hour_now = (datetime.now()).strftime('%H')
        minute_now = (datetime.now()).strftime('%M')
        status = updatedata.getsql('select auto1 from status_control')
        if status[0] == 1:
            time1 = updatedata.getsql("select * from time1")
            if datastatus.count1 == 0:
                if int(time1[0][:2]) < int(time1[1][:2]):
                    if ((int(hour_now) >= int(time1[0][:2])) and (int(hour_now) <= int(time1[1][:2]))) :
                        if int(hour_now) == int(time1[0][:2]):
                            if int(minute_now) >= int(time1[0][3:5]):
                                gettime(time1[0], time1[1], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[1][:2]):
                            if int(minute_now) <= int(time1[1][3:5]):
                                gettime(time1[0], time1[1], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 1
                        else:
                            gettime(time1[0], time1[1], 1)
                    else:
                        datastatus.count1 = 1
                        gettime("00:00", "00:00", 0)
                elif int(time1[0][:2]) > int(time1[1][:2]):
                    if ((int(hour_now) >= int(time1[0][:2])) or (int(hour_now) <= int(time1[1][:2]))) :
                        if int(hour_now) == int(time1[0][:2]):
                            if int(minute_now) >= int(time1[0][3:5]):
                                gettime(time1[0], time1[1], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[1][:2]):
                            if int(minute_now) <= int(time1[1][3:5]):
                                gettime(time1[0], time1[1], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 1
                        else:
                            gettime(time1[0], time1[1], 1)
                    else:
                        datastatus.count1 = 1
                        gettime("00:00", "00:00", 0)
                else:
                    datastatus.count1 = 1
            elif datastatus.count1 == 1:
                if int(time1[4][:2]) < int(time1[5][:2]):
                    if (int(hour_now) >= int(time1[4][:2])) and (int(hour_now) <= int(time1[5][:2])):
                        if int(hour_now) == int(time1[4][:2]):
                            if int(minute_now) >= int(time1[4][3:5]):
                                gettime(time1[4], time1[5], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[5][:2]):
                            if int(minute_now) <= int(time1[5][3:5]):
                                gettime(time1[4], time1[5], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 2
                        else:
                            gettime(time1[4], time1[5], 1)
                    else:
                        datastatus.count1 = 2
                        gettime("00:00", "00:00", 0)
                elif int(time1[4][:2]) > int(time1[5][:2]):
                    if (int(hour_now) >= int(time1[4][:2])) or (int(hour_now) <= int(time1[5][:2])):
                        if int(hour_now) == int(time1[4][:2]):
                            if int(minute_now) >= int(time1[4][3:5]):
                                gettime(time1[4], time1[5], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[5][:2]):
                            if int(minute_now) <= int(time1[5][3:5]):
                                gettime(time1[4], time1[5], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 2
                        else:
                            gettime(time1[4], time1[5], 1)
                    else:
                        datastatus.count1 = 2
                        gettime("00:00", "00:00", 0)
                else:
                    datastatus.count1 = 2
            elif datastatus.count1 == 2: 
                if int(time1[8][:2]) < int(time1[9][:2]):
                    if (int(hour_now) >= int(time1[8][:2])) and (int(hour_now) <= int(time1[9][:2])):
                        if int(hour_now) == int(time1[8][:2]):
                            if int(minute_now) >= int(time1[8][3:5]):
                                gettime(time1[8], time1[9], 1)
                            else: 
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[9][:2]):
                            if int(minute_now) <= int(time1[9][3:5]):
                                gettime(time1[8], time1[9], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 3
                        else: 
                            gettime(time1[8], time1[9], 1)
                    else:
                        datastatus.count1 = 3
                        gettime("00:00", "00:00", 0)
                elif int(time1[8][:2]) > int(time1[9][:2]):
                    if (int(hour_now) >= int(time1[8][:2])) or (int(hour_now) <= int(time1[9][:2])):
                        if int(hour_now) == int(time1[8][:2]):
                            if int(minute_now) >= int(time1[8][3:5]):
                                gettime(time1[8], time1[9], 1)
                            else: 
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[9][:2]):
                            if int(minute_now) <= int(time1[9][3:5]):
                                gettime(time1[8], time1[9], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 3
                        else: 
                            gettime(time1[8], time1[9], 1)
                    else:
                        datastatus.count1 = 3
                        gettime("00:00", "00:00", 0)
                else:
                    datastatus.count1 = 3
            elif datastatus.count1 == 3:
                if int(time1[12][:2]) < int(time1[13][:2]):
                    if (int(hour_now) >= int(time1[12][:2]) and int(hour_now) <= int(time1[13][:2])):
                        if int(hour_now) == int(time1[12][:2]):
                            if int(minute_now) >= int(time1[12][3:5]):
                                gettime(time1[12], time1[13], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[13][:2]):
                            if int(minute_now) <= int(time1[13][3:5]):
                                gettime(time1[12], time1[13], 1)
                            else: 
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 0
                        else:
                            gettime(time1[12], time1[13], 1)
                    else:
                        datastatus.count1 = 0
                        gettime("00:00", "00:00", 0)   
                elif int(time1[12][:2]) > int(time1[13][:2]):
                    if (int(hour_now) >= int(time1[12][:2]) or int(hour_now) <= int(time1[13][:2])):
                        if int(hour_now) == int(time1[12][:2]):
                            if int(minute_now) >= int(time1[12][3:5]):
                                gettime(time1[12], time1[13], 1)
                            else:
                                gettime("00:00", "00:00", 0)
                        elif int(hour_now) == int(time1[13][:2]):
                            if int(minute_now) <= int(time1[13][3:5]):
                                gettime(time1[12], time1[13], 1)
                            else: 
                                gettime("00:00", "00:00", 0)
                                datastatus.count1 = 0
                        else:
                            gettime(time1[12], time1[13], 1)
                    else:
                        datastatus.count1 = 0
                        gettime("00:00", "00:00", 0)   
                else:
                    datastatus.count1 = 0              
        else:
            gettime("00:00", "00:00", datastatus.manual1)


def logo_branch2():
    def gettime1(start, stop, light):
        datasend.dttimecontrol.start2 = start
        datasend.dttimecontrol.stop2 = stop
        datasend.dtlightstatus.light2 = light

    if (datastatus.permission == 1):
        hour_now = (datetime.now()).strftime('%H')
        minute_now = (datetime.now()).strftime('%M')
        status = updatedata.getsql('select auto2 from status_control')
        if status[0] == 1:
            time2 = updatedata.getsql("select * from time2")
            if datastatus.count2 == 0:
                if int(time2[0][:2]) < int(time2[1][:2]):
                    if (int(hour_now) >= int(time2[0][:2])) and (int(hour_now) <= int(time2[1][:2])):
                        if int(hour_now) == int(time2[0][:2]):
                            if int(minute_now) >= int(time2[0][3:5]):
                                gettime1(time2[0], time2[1], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[1][:2]):
                            if int(minute_now) <= int(time2[1][3:5]):
                                gettime1(time2[0], time2[1], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 1
                        else:
                            gettime1(time2[0], time2[1], 1)
                    else: 
                        datastatus.count2 = 1
                        gettime1("00:00", "00:00", 0)
                elif int(time2[0][:2]) > int(time2[1][:2]):
                    if (int(hour_now) >= int(time2[0][:2])) or (int(hour_now) <= int(time2[1][:2])):
                        if int(hour_now) == int(time2[0][:2]):
                            if int(minute_now) >= int(time2[0][3:5]):
                                gettime1(time2[0], time2[1], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[1][:2]):
                            if int(minute_now) <= int(time2[1][3:5]):
                                gettime1(time2[0], time2[1], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 1
                        else:
                            gettime1(time2[0], time2[1], 1)
                    else: 
                        datastatus.count2 = 1
                        gettime1("00:00", "00:00", 0)
                else:
                    datastatus.count2 = 1
            elif datastatus.count2 == 1:
                if int(time2[4][:2]) < int(time2[5][:2]):
                    if (int(hour_now) >= int(time2[4][:2])) and (int(hour_now) <= int(time2[5][:2])):
                        if int(hour_now) == int(time2[4][:2]):
                            if int(minute_now) >= int(time2[4][3:5]):
                                gettime1(time2[4], time2[5], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[5][:2]):
                            if int(minute_now) <= int(time2[5][3:5]):
                                gettime1(time2[4], time2[5], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 2
                        else:
                            gettime1(time2[4], time2[5], 1)
                    else: 
                        datastatus.count2 = 2
                        gettime1("00:00", "00:00", 0)
                elif int(time2[4][:2]) > int(time2[5][:2]):
                    if (int(hour_now) >= int(time2[4][:2])) or (int(hour_now) <= int(time2[5][:2])):
                        if int(hour_now) == int(time2[4][:2]):
                            if int(minute_now) >= int(time2[4][3:5]):
                                gettime1(time2[4], time2[5], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[5][:2]):
                            if int(minute_now) <= int(time2[5][3:5]):
                                gettime1(time2[4], time2[5], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 2
                        else:
                            gettime1(time2[4], time2[5], 1)
                    else: 
                        datastatus.count2 = 2
                        gettime1("00:00", "00:00", 0)
                else: 
                    datastatus.count2 = 2
            elif datastatus.count2 == 2:
                if int(time2[8][:2]) < int(time2[9][:2]):
                    if (int(hour_now) >= int(time2[8][:2])) and (int(hour_now) <= int(time2[9][:2])):
                        if int(hour_now) == int(time2[8][:2]):
                            if int(minute_now) >= int(time2[8][3:5]):
                                gettime1(time2[8], time2[9], 1)
                            else: 
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[9][:2]):
                            if int(minute_now) <= int(time2[9][3:5]):
                                gettime1(time2[8], time2[9], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 3
                        else: 
                            gettime1(time2[8], time2[9], 1)
                    else: 
                        datastatus.count2 = 3
                        gettime1("00:00", "00:00", 0)
                elif int(time2[8][:2]) > int(time2[9][:2]):
                    if (int(hour_now) >= int(time2[8][:2])) or (int(hour_now) <= int(time2[9][:2])):
                        if int(hour_now) == int(time2[8][:2]):
                            if int(minute_now) >= int(time2[8][3:5]):
                                gettime1(time2[8], time2[9], 1)
                            else: 
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[9][:2]):
                            if int(minute_now) <= int(time2[9][3:5]):
                                gettime1(time2[8], time2[9], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 3
                        else: 
                            gettime1(time2[8], time2[9], 1)
                    else: 
                        datastatus.count2 = 3
                        gettime1("00:00", "00:00", 0)
                else:
                    datastatus.count2 = 3
            elif datastatus.count2 == 3:
                if int(time2[12][:2]) < int(time2[13][:2]):
                    if (int(hour_now) >= int(time2[12][:2])) and (int(hour_now) <= int(time2[13][:2])):
                        if int(hour_now) == int(time2[12][:2]):
                            if int(minute_now) >= int(time2[12][3:5]):
                                gettime1(time2[12], time2[13], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[13][:2]):
                            if int(minute_now) <= int(time2[13][3:5]):
                                gettime1(time2[12], time2[13], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 0
                        else:
                            gettime1(time2[12], time2[13], 1)
                    else: 
                        datastatus.count2 = 0
                        gettime1("00:00", "00:00", 0)
                elif int(time2[12][:2]) > int(time2[13][:2]):
                    if (int(hour_now) >= int(time2[12][:2])) and (int(hour_now) <= int(time2[13][:2])):
                        if int(hour_now) == int(time2[12][:2]):
                            if int(minute_now) >= int(time2[12][3:5]):
                                gettime1(time2[12], time2[13], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                        elif int(hour_now) == int(time2[13][:2]):
                            if int(minute_now) <= int(time2[13][3:5]):
                                gettime1(time2[12], time2[13], 1)
                            else:
                                gettime1("00:00", "00:00", 0)
                                datastatus.count2 = 0
                        else:
                            gettime1(time2[12], time2[13], 1)
                    else: 
                        datastatus.count2 = 0
                        gettime1("00:00", "00:00", 0)
                else:
                    datastatus.count2 = 0      
        else:
            gettime1("00:00", "00:00", datastatus.manual2)
            
            
def logo_branch3():
    def gettime2(start, stop, light):
        datasend.dttimecontrol.start3 = start
        datasend.dttimecontrol.stop3 = stop
        datasend.dtlightstatus.light3 = light

    if (datastatus.permission == 1):
        hour_now = (datetime.now()).strftime('%H')
        minute_now = (datetime.now()).strftime('%M')
        status = updatedata.getsql('select auto3 from status_control')
        if status[0] == 1:
            time3 = updatedata.getsql("select * from time3")
            if datastatus.count3 == 0:
                if int(time3[0][:2]) < int(time3[1][:2]):
                    if (int(hour_now) >= int(time3[0][:2])) and (int(hour_now) <= int(time3[1][:2])):
                        if int(hour_now) == int(time3[0][:2]):
                            if int(minute_now) >= int(time3[0][3:5]):
                                gettime2(time3[0], time3[1], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[1][:2]):
                            if int(minute_now) <= int(time3[1][3:5]):
                                gettime2(time3[0], time3[1], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 1
                        else:
                            gettime2(time3[0], time3[1], 1)
                    else:
                        datastatus.count3 = 1
                        gettime2("00:00", "00:00", 0)
                elif int(time3[0][:2]) > int(time3[1][:2]):
                    if (int(hour_now) >= int(time3[0][:2])) or (int(hour_now) <= int(time3[1][:2])):
                        if int(hour_now) == int(time3[0][:2]):
                            if int(minute_now) >= int(time3[0][3:5]):
                                gettime2(time3[0], time3[1], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[1][:2]):
                            if int(minute_now) <= int(time3[1][3:5]):
                                gettime2(time3[0], time3[1], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 1
                        else:
                            gettime2(time3[0], time3[1], 1)
                    else: 
                        datastatus.count3 = 1
                        gettime2("00:00", "00:00", 0)
                else:
                    datastatus.count3 = 1
            elif datastatus.count3 == 1:
                if int(time3[4][:2]) < int(time3[5][:2]):
                    if (int(hour_now) >= int(time3[4][:2])) and (int(hour_now) <= int(time3[5][:2])):
                        if int(hour_now) == int(time3[4][:2]):
                            if int(minute_now) >= int(time3[4][3:5]):
                                gettime2(time3[4], time3[5], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[5][:2]):
                            if int(minute_now) <= int(time3[5][3:5]):
                                gettime2(time3[4], time3[5], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 2
                        else:
                            gettime2(time3[4], time3[5], 1)
                    else:
                        datastatus.count3 = 2
                        gettime2("00:00", "00:00", 0)
                elif int(time3[4][:2]) > int(time3[5][:2]):
                    if (int(hour_now) >= int(time3[4][:2])) or (int(hour_now) <= int(time3[5][:2])):
                        if int(hour_now) == int(time3[4][:2]):
                            if int(minute_now) >= int(time3[4][3:5]):
                                gettime2(time3[4], time3[5], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[5][:2]):
                            if int(minute_now) <= int(time3[5][3:5]):
                                gettime2(time3[4], time3[5], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 2
                        else:
                            gettime2(time3[4], time3[5], 1)
                    else:
                        datastatus.count3 = 2
                        gettime2("00:00", "00:00", 0)
                else:
                    datastatus.count3 = 2
            elif datastatus.count3 == 2:
                if int(time3[8][:2]) < int(time3[9][:2]):
                    if (int(hour_now) >= int(time3[8][:2])) and (int(hour_now) <= int(time3[9][:2])):
                        if int(hour_now) == int(time3[8][:2]):
                            if int(minute_now) >= int(time3[8][3:5]):
                                gettime2(time3[8], time3[9], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[9][:2]):
                            if int(minute_now) <= int(time3[9][3:5]):
                                gettime2(time3[8], time3[9], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 3
                        else: 
                            gettime2(time3[8], time3[9], 1)
                    else: 
                        datastatus.count3 = 3
                        gettime2("00:00", "00:00", 0)
                elif int(time3[8][:2]) > int(time3[9][:2]):
                    if (int(hour_now) >= int(time3[8][:2])) or (int(hour_now) <= int(time3[9][:2])):
                        if int(hour_now) == int(time3[8][:2]):
                            if int(minute_now) >= int(time3[8][3:5]):
                                gettime2(time3[8], time3[9], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[9][:2]):
                            if int(minute_now) <= int(time3[9][3:5]):
                                gettime2(time3[8], time3[9], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 3
                        else: 
                            gettime2(time3[8], time3[9], 1)
                    else: 
                        datastatus.count3 = 3
                        gettime2("00:00", "00:00", 0)
                else:
                    datastatus.count3 = 3
            elif datastatus.count3 == 3:
                if int(time3[12][:2]) < int(time3[13][:2]):
                    if (int(hour_now) >= int(time3[12][:2])) and (int(hour_now) <= int(time3[13][:2])):
                        if int(hour_now) == int(time3[12][:2]):
                            if int(minute_now) >= int(time3[12][3:5]):
                                gettime2(time3[12], time3[13], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[13][:2]):
                            if int(minute_now) <= int(time3[13][3:5]):
                                gettime2(time3[12], time3[13], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 0
                        else:
                            gettime2(time3[12], time3[13], 1)
                    else: 
                        datastatus.count3 = 0
                        gettime2("00:00", "00:00", 0)
                elif int(time3[12][:2]) > int(time3[13][:2]):
                    if (int(hour_now) >= int(time3[12][:2])) or (int(hour_now) <= int(time3[13][:2])):
                        if int(hour_now) == int(time3[12][:2]):
                            if int(minute_now) >= int(time3[12][3:5]):
                                gettime2(time3[12], time3[13], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                        elif int(hour_now) == int(time3[13][:2]):
                            if int(minute_now) <= int(time3[13][3:5]):
                                gettime2(time3[12], time3[13], 1)
                            else:
                                gettime2("00:00", "00:00", 0)
                                datastatus.count3 = 0
                        else:
                            gettime2(time3[12], time3[13], 1)
                    else: 
                        datastatus.count3 = 0
                        gettime2("00:00", "00:00", 0)
                else:
                    datastatus.count3 = 0
        else:
            gettime2("00:00", "00:00", datastatus.manual3)
        

def logo_branch4():
    def gettime3(start, stop ,light):
        datasend.dttimecontrol.start4 = start
        datasend.dttimecontrol.stop4 = stop
        datasend.dtlightstatus.light4 = light
    
    if (datastatus.permission == 1):
        hour_now = (datetime.now()).strftime('%H')
        minute_now = (datetime.now()).strftime('%M')
        status = updatedata.getsql('select auto4 from status_control')
        if status[0] == 1:
            time4 = updatedata.getsql("select * from time4")
            if datastatus.count4 == 0:
                if int(time4[0][:2]) < int(time4[1][:2]): 
                    if ((int(hour_now) >= int(time4[0][:2])) and (int(hour_now) <= int(time4[1][:2]))):
                        if int(hour_now) == int(time4[0][:2]):
                            if int(minute_now) >= int(time4[0][3:5]):
                                gettime3(time4[0], time4[1], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[1][:2]):
                            if int(minute_now) <= int(time4[1][3:5]):
                                gettime3(time4[0], time4[1], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 1
                        else:
                            gettime3(time4[0], time4[1], 1)
                    else: 
                        datastatus.count4 = 1
                        gettime3("00:00", "00:00", 0)
                elif int(time4[0][:2]) > int(time4[1][:2]):
                    if ((int(hour_now) >= int(time4[0][:2])) or (int(hour_now) <= int(time4[1][:2]))):
                        if int(hour_now) == int(time4[0][:2]):
                            if int(minute_now) >= int(time4[0][3:5]):
                                gettime3(time4[0], time4[1], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[1][:2]):
                            if int(minute_now) <= int(time4[1][3:5]):
                                gettime3(time4[0], time4[1], 1)
                                datastatus.count4 = 1
                            else:
                                gettime3("00:00", "00:00", 0)
                        else:
                            gettime3(time4[0], time4[1], 1)
                    else: 
                        datastatus.count4 = 1
                        gettime3("00:00", "00:00", 0)
                else:
                    datastatus.count4 = 1
            elif datastatus.count4 == 1:
                if int(time4[4][:2]) < int(time4[5][:2]):
                    if (int(hour_now) >= int(time4[4][:2])) and (int(hour_now) <= int(time4[5][:2])):
                        if int(hour_now) == int(time4[4][:2]):
                            if int(minute_now) >= int(time4[4][3:5]):
                                gettime3(time4[4], time4[5], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[5][:2]):
                            if int(minute_now) <= int(time4[5][3:5]):
                                gettime3(time4[4], time4[5], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 2
                        else:
                            gettime3(time4[4], time4[5], 1)
                    else: 
                        datastatus.count4 = 2
                        gettime3("00:00", "00:00", 0)
                elif int(time4[4][:2]) > int(time4[5][:2]):
                    if (int(hour_now) >= int(time4[4][:2])) or (int(hour_now) <= int(time4[5][:2])):
                        if int(hour_now) == int(time4[4][:2]):
                            if int(minute_now) >= int(time4[4][3:5]):
                                gettime3(time4[4], time4[5], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[5][:2]):
                            if int(minute_now) <= int(time4[5][3:5]):
                                gettime3(time4[4], time4[5], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 2
                        else:
                            gettime3(time4[4], time4[5], 1)
                    else: 
                        datastatus.count4 = 2
                        gettime3("00:00", "00:00", 0)
                else:
                    datastatus.count4 = 2
            elif datastatus.count4 == 2:
                if int(time4[8][:2]) < int(time4[9][:2]):
                    if (int(hour_now) >= int(time4[8][:2])) and (int(hour_now) <= int(time4[9][:2])):
                        if int(hour_now) == int(time4[8][:2]):
                            if int(minute_now) >= int(time4[8][3:5]):
                                gettime3(time4[8], time4[9], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[9][:2]):
                            if int(minute_now) <= int(time4[9][3:5]):
                                gettime3(time4[8], time4[9], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 3
                        else: 
                            gettime3(time4[8], time4[9], 1)
                    else:
                        datastatus.count4 = 3
                        gettime3("00:00", "00:00", 0)
                elif int(time4[8][:2]) > int(time4[9][:2]):
                    if (int(hour_now) >= int(time4[8][:2])) or (int(hour_now) <= int(time4[9][:2])):
                        if int(hour_now) == int(time4[8][:2]):
                            if int(minute_now) >= int(time4[8][3:5]):
                                gettime3(time4[8], time4[9], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[9][:2]):
                            if int(minute_now) <= int(time4[9][3:5]):
                                gettime3(time4[8], time4[9], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 3
                        else: 
                            gettime3(time4[8], time4[9], 1)
                    else:
                        datastatus.count4 = 3
                        gettime3("00:00", "00:00", 0)
                else:
                    datastatus.count4 = 3
            elif datastatus.count4 == 3:
                if int(time4[12][:2]) < int(time4[13][:2]):
                    if (int(hour_now) >= int(time4[12][:2])) and (int(hour_now) <= int(time4[13][:2])):
                        if int(hour_now) == int(time4[12][:2]):
                            if int(minute_now) >= int(time4[12][3:5]):
                                gettime3(time4[12], time4[13], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[13][:2]):
                            if int(minute_now) <= int(time4[13][3:5]):
                                gettime3(time4[12], time4[13], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 0
                        else:
                            gettime3(time4[12], time4[13], 1)
                    else: 
                        datastatus.count4 = 0
                        gettime3("00:00", "00:00", 0)
                elif int(time4[12][:2]) > int(time4[13][:2]):
                    if (int(hour_now) >= int(time4[12][:2])) or (int(hour_now) <= int(time4[13][:2])):
                        if int(hour_now) == int(time4[12][:2]):
                            if int(minute_now) >= int(time4[12][3:5]):
                                gettime3(time4[12], time4[13], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                        elif int(hour_now) == int(time4[13][:2]):
                            if int(minute_now) <= int(time4[13][3:5]):
                                gettime3(time4[12], time4[13], 1)
                            else:
                                gettime3("00:00", "00:00", 0)
                                datastatus.count4 = 0
                        else:
                            gettime3(time4[12], time4[13], 1)
                    else: 
                        datastatus.count4 = 0
                        gettime3("00:00", "00:00", 0)
                else:
                    datastatus.count4 = 0
        else:
            gettime3("00:00", "00:00", datastatus.manual4)
        
#option = 1 for S7_1200, option = 2 for Logo
def ui1_max(dt):
    option = checkoption()
    if (datastatus.permission == 1):
        if(dt[0] == "u1_1max"):
            if option == 1:
                shiftdt_S71200(1,52,int(dt[1]))
        elif(dt[0] == "i1_1max"):
            if option == 1:
                shiftdt_S71200(1,53,int(dt[1]))
        elif(dt[0] == "u1_2max"):
            if option == 1:
                shiftdt_S71200(1,64,int(dt[1]))
        elif(dt[0] == "i1_2max"):
            if option == 1:
                shiftdt_S71200(1,65,int(dt[1]))
        elif(dt[0] == "u1_3max"):
            if option == 1:
                shiftdt_S71200(1,76,int(dt[1]))
        elif(dt[0] == "i1_3max"):
            if option == 1:
                shiftdt_S71200(1,77,int(dt[1]))
        elif(dt[0] == "u1_4max"):
            if option == 1:
                shiftdt_S71200(1,88,int(dt[1]))
        elif(dt[0] == "i1_4max"):
            if option == 1:
                shiftdt_S71200(1,89,int(dt[1]))
def ui2_max(dt):
    option = checkoption()
    if (datastatus.permission == 1):
        if(dt[0] == "u2_1max"):
            if option == 1:
                shiftdt_S71200(1,100,int(dt[1]))
        elif(dt[0] == "i2_1max"):
            if option == 1:
                shiftdt_S71200(1,101,int(dt[1]))
        elif(dt[0] == "u2_2max"):
            if option == 1:
                shiftdt_S71200(1,112,int(dt[1]))
        elif(dt[0] == "i2_2max"):
            if option == 1:
                shiftdt_S71200(1,113,int(dt[1]))
        elif(dt[0] == "u2_3max"):
            if option == 1:
                shiftdt_S71200(1,124,int(dt[1]))
        elif(dt[0] == "i2_3max"):
            if option == 1:
                shiftdt_S71200(1,125,int(dt[1]))
        elif(dt[0] == "u2_4max"):
            if option == 1:
                shiftdt_S71200(1,136,int(dt[1]))
        elif(dt[0] == "i2_4max"):
            if option == 1:
                shiftdt_S71200(1,137,int(dt[1]))
def ui3_max(dt):
    option = checkoption()
    if (datastatus.permission == 1):
        if(dt[0] == "u3_1max"):
            if option == 1:
                shiftdt_S71200(1,148,int(dt[1]))
        elif(dt[0] == "i3_1max"):
            if option == 1:
                shiftdt_S71200(1,149,int(dt[1]))
        elif(dt[0] == "u3_2max"):
            if option == 1:
                shiftdt_S71200(1,160,int(dt[1]))
        elif(dt[0] == "i3_2max"):
            if option == 1:
                shiftdt_S71200(1,161,int(dt[1]))
        elif(dt[0] == "u3_3max"):
            if option == 1:
                shiftdt_S71200(1,172,int(dt[1]))
        elif(dt[0] == "i3_3max"):
            if option == 1:
                shiftdt_S71200(1,173,int(dt[1]))
        elif(dt[0] == "u3_4max"):
            if option == 1:
                shiftdt_S71200(1,184,int(dt[1]))
        elif(dt[0] == "i3_4max"):
            if option == 1:
                shiftdt_S71200(1,185,int(dt[1]))
def ui4_max(dt):
    option = checkoption()
    if (datastatus.permission == 1):
        if(dt[0] == "u4_1max"):
            if option == 1:
                shiftdt_S71200(1,196,int(dt[1]))
        elif(dt[0] == "i4_1max"):
            if option == 1:
                shiftdt_S71200(1,197,int(dt[1]))
        elif(dt[0] == "u4_2max"):
            if option == 1:
                shiftdt_S71200(1,208,int(dt[1]))
        elif(dt[0] == "i4_2max"):
            if option == 1:
                shiftdt_S71200(1,209,int(dt[1]))
        elif(dt[0] == "u4_3max"):
            if option == 1:
                shiftdt_S71200(1,220,int(dt[1]))
        elif(dt[0] == "i4_3max"):
            if option == 1:
                shiftdt_S71200(1,221,int(dt[1]))
        elif(dt[0] == "u4_4max"):
            if option == 1:
                shiftdt_S71200(1,232,int(dt[1]))
        elif(dt[0] == "i4_4max"):
            if option == 1:
                shiftdt_S71200(1,233,int(dt[1]))

def setdatetime(dt):
    start = 12
    option = checkoption()
    if (datastatus.permission == 1):
        if (option == 1):
            hyear = (int(dt[0:4])&(0xff00))>>8
            shiftdt_S71200(2,start,hyear)
            lyear = (int(dt[0:4]))&(0x00ff)
            shiftdt_S71200(2,start+1,lyear)
            shiftdt_S71200(2,start+2,int(dt[5:7]))
            shiftdt_S71200(2,start+3,int(dt[8:10]))
            shiftdt_S71200(2,start+5,int(dt[11:13]))
            shiftdt_S71200(2,start+6,int(dt[14:16]))
            shiftdt_S71200(2,start+7,0)
            plcS7_1200.mbwrite_bool(2,1,0,True)
            time.sleep(0.1)
            plcS7_1200.mbwrite_bool(2,1,1,False)
        elif option == 2:
            connect_plcLogo.send_datatoPLC("V985",int(dt[2:4]))
            connect_plcLogo.send_datatoPLC("V986",int(dt[5:7]))
            connect_plcLogo.send_datatoPLC("V987", int(dt[8:10]))
            connect_plcLogo.send_datatoPLC("V988",int(dt[11:13]))
            connect_plcLogo.send_datatoPLC("V989", int(dt[14:16]))



#setting branch1
def branch1time(dt, s_tr, dt1):
    option = checkoption()
    if (datastatus.permission == 1):
        hour = int(int(s_tr) / 100) 
        minute  = int(int(s_tr) % 100)
        if (dt == "starttime1-branch1"):
            if (option == 1):
                shiftdt_S71200(1,48,hour)
                shiftdt_S71200(1,49,minute)
            elif option == 2:
                shiftdt_Logo("VW0",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET start1_1=?",(dt1,))
        elif (dt == "stoptime1-branch1"):
            if (option == 1):
                shiftdt_S71200(1,50,hour)
                shiftdt_S71200(1,51,minute)
            elif option == 2:
                shiftdt_Logo("VW2",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET stop1_1=?",(dt1,))
        elif (dt == "starttime2-branch1"):
            if option == 1:
                shiftdt_S71200(1,60,hour)
                shiftdt_S71200(1,61,minute)
            elif option == 2:
                shiftdt_Logo("VW4",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET start1_2=?",(dt1,))
        elif (dt == "stoptime2-branch1"): 
            if option == 1:
                shiftdt_S71200(1,62,hour)
                shiftdt_S71200(1,63,minute)
            elif option == 2:
                shiftdt_Logo("VW6",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET stop1_2=?",(dt1,))
        elif (dt == "starttime3-branch1"):
            if option == 1:
                shiftdt_S71200(1,72,hour)
                shiftdt_S71200(1,73,minute)
            elif option == 2:
                shiftdt_Logo("VW8",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET start1_3=?",(dt1,))
        elif (dt == "stoptime3-branch1"):
            if option == 1:
                shiftdt_S71200(1,74,hour)
                shiftdt_S71200(1,75,minute)
            elif option == 2:
                shiftdt_Logo("VW10",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET stop1_3=?",(dt1,))
        elif (dt == "starttime4-branch1"):
            if option == 1:
                shiftdt_S71200(1,84,hour)
                shiftdt_S71200(1,85,minute)
            elif option == 2:
                shiftdt_Logo("VW12",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET start1_4=?",(dt1,))
        elif (dt == "stoptime4-branch1"):
            if option == 1:
                shiftdt_S71200(1,86,hour)
                shiftdt_S71200(1,87,minute)
            elif option == 2:
                shiftdt_Logo("VW14",int(s_tr))
            updatedata.sqlupdate("UPDATE time1 SET stop1_4=?",(dt1,))
#Branch1 finish

#Branch2 start
def branch2time(dt, s_tr, dt1):
    option = checkoption() 
    hour = int(int(s_tr) / 100)
    minute = int(int(s_tr) % 100)
    if datastatus.permission == 1:
        if (dt == "starttime1-branch2"):
            if option == 1: 
                shiftdt_S71200(1,96,hour)
                shiftdt_S71200(1,97,minute)
            elif option == 2:
                shiftdt_Logo("VW16",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET start2_1=?",(dt1,))
        elif (dt == "stoptime1-branch2"):
            if option == 1:
                shiftdt_S71200(1,98,hour)
                shiftdt_S71200(1,99,minute)
            elif option == 2:
                shiftdt_Logo("VW18",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET stop2_1=?",(dt1,))
        elif (dt == "starttime2-branch2"):
            if option == 1:
                shiftdt_S71200(1,108,hour)
                shiftdt_S71200(1,109,minute)
            elif option == 2:
                shiftdt_Logo("VW20",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET start2_2=?",(dt1,))
        elif (dt == "stoptime2-branch2"): 
            if option == 1:
                shiftdt_S71200(1,110,hour)
                shiftdt_S71200(1,111,minute)
            elif option == 2:
                shiftdt_Logo("VW22",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET stop2_2=?",(dt1,))
        elif (dt == "starttime3-branch2"):
            if option == 1:
                shiftdt_S71200(1,120,hour)
                shiftdt_S71200(1,121,minute)
            elif option == 2:
                shiftdt_Logo("VW24",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET start2_3=?",(dt1,))
        elif (dt == "stoptime3-branch2"):
            if option == 1:
                shiftdt_S71200(1,122,hour)
                shiftdt_S71200(1,123,minute)
            elif option == 2:
                shiftdt_Logo("VW26",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET stop2_3=?",(dt1,))
        elif (dt == "starttime4-branch2"):
            if option == 1:
                shiftdt_S71200(1,132,hour)
                shiftdt_S71200(1,133,minute)
            elif option == 2:
                shiftdt_Logo("VW28",int(s_tr))
            updatedata.sqlupdate("UPDATE time2 SET start2_4=?",(dt1,))
        elif (dt == "stoptime4-branch2"):
            if option == 1:
                shiftdt_S71200(1,134,hour)
                shiftdt_S71200(1,135,minute)
            elif option == 2:
                shiftdt_Logo("VW30",int(s_tr))   
            updatedata.sqlupdate("UPDATE time2 SET stop2_4=?",(dt1,))
#
#Branch3 start
def branch3time(dt,s_tr, dt1): 
    option = checkoption()
    hour = int(int(s_tr) / 100)
    minute = int(int(s_tr) % 100)
    if datastatus.permission == 1:
        if (dt == "starttime1-branch3"):
            if option == 1:
                shiftdt_S71200(1,144,hour)
                shiftdt_S71200(1,145,minute)
            elif option == 2:
                shiftdt_Logo("VW32",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET start3_1=?",(dt1,))
        elif (dt == "stoptime1-branch3"):
            if option == 1:
                shiftdt_S71200(1,146,hour)
                shiftdt_S71200(1,147,minute)
            elif option == 2:
                shiftdt_Logo("VW34",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET stop3_1=?",(dt1,))
        elif (dt == "starttime2-branch3"):
            if option == 1:
                shiftdt_S71200(1,156,hour)
                shiftdt_S71200(1,157,minute)
            elif option == 2:
                shiftdt_Logo("VW36",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET start3_2=?",(dt1,))
        elif (dt == "stoptime2-branch3"): 
            if option == 1:
                shiftdt_S71200(1,158,hour)
                shiftdt_S71200(1,159,minute)
            elif option == 2:
                shiftdt_Logo("VW38",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET stop3_2=?",(dt1,))
        elif (dt == "starttime3-branch3"):
            if option == 1:
                shiftdt_S71200(1,168,hour)
                shiftdt_S71200(1,169,minute)
            elif option == 2:
                shiftdt_Logo("VW40",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET start3_3=?",(dt1,))
        elif (dt == "stoptime3-branch3"):
            if option == 1:
                shiftdt_S71200(1,170,hour)
                shiftdt_S71200(1,171,minute)
            elif option == 2:
                shiftdt_Logo("VW42",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET stop3_3=?",(dt1,))
        elif (dt == "starttime4-branch3"):
            if option == 1:
                shiftdt_S71200(1,180,hour)
                shiftdt_S71200(1,181,minute)
            elif option == 2:
                shiftdt_Logo("VW44",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET start3_4=?",(dt1,))
        elif (dt == "stoptime4-branch3"):
            if option == 1:
                shiftdt_S71200(1,182,hour)
                shiftdt_S71200(1,183,minute)
            elif option == 2:
                shiftdt_Logo("VW46",int(s_tr))
            updatedata.sqlupdate("UPDATE time3 SET stop3_4=?",(dt1,))
#Branch3 finish

#Branch4 start
def branch4time(dt, s_tr, dt1):
    option = checkoption()
    hour = int(int(s_tr) / 100)
    minute = int(int(s_tr) % 100)
    if datastatus.permission == 1: 
        if (dt == "starttime1-branch4"):
            if option == 1:
                shiftdt_S71200(1,192,hour)
                shiftdt_S71200(1,193,minute)
            elif option == 2:
                shiftdt_Logo("VW48",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET start4_1=?",(dt1,))
        elif (dt == "stoptime1-branch4"):
            if option == 1:
                shiftdt_S71200(1,194,hour)
                shiftdt_S71200(1,195,minute)
            elif option == 2:
                shiftdt_Logo("VW50",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET stop4_1=?",(dt1,))
        elif (dt == "starttime2-branch4"):
            if option == 1:
                shiftdt_S71200(1,204,hour)
                shiftdt_S71200(1,205,minute)
            elif option == 2:
                shiftdt_Logo("VW52",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET start4_2=?",(dt1,))
        elif (dt == "stoptime2-branch4"): 
            if option == 1:
                shiftdt_S71200(1,206,hour)
                shiftdt_S71200(1,207,minute)
            elif option == 2:
                shiftdt_Logo("VW54",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET stop4_2=?",(dt1,))
        elif (dt == "starttime3-branch4"):
            if option == 1:
                shiftdt_S71200(1,216,hour)
                shiftdt_S71200(1,217,minute)
            elif option == 2:
                shiftdt_Logo("VW56",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET start4_3=?",(dt1,))
        elif (dt == "stoptime3-branch4"):
            if option == 1:
                shiftdt_S71200(1,218,hour)
                shiftdt_S71200(1,219,minute)
            elif option == 2:
                shiftdt_Logo("VW58",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET stop4_3=?",(dt1,))
        elif (dt == "starttime4-branch4"):
            if option == 1:
                shiftdt_S71200(1,228,hour)
                shiftdt_S71200(1,229,minute)
            elif option == 2:
                shiftdt_Logo("VW60",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET start4_4=?",(dt1,))
        elif (dt == "stoptime4-branch4"):
            if option == 1:
                shiftdt_S71200(1,230,hour)
                shiftdt_S71200(1,231,minute)
            elif option == 2:
                shiftdt_Logo("VW62",int(s_tr))
            updatedata.sqlupdate("UPDATE time4 SET start4_4=?",(dt1,))
#Branch4 finish

def delete(dt):
    option = checkoption()
    val = ("0","0",0,0,"0","0",0,0,"0","0",0,0,"0","0",0,0)
    if dt == "delete1":
        if option == 1:
            plcS7_1200.mbwrite_bool(3,1,2,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(3,1,2,False)
            time.sleep(0.5)
        elif option == 2:
            logotime1(val)
        datamanage.fl_time1 = 1
        sql = "UPDATE time1 SET start1_1=?,stop1_1=?,u1_1=?,i1_1=?,start1_2=?,stop1_2=?,u1_2=?,i1_2=?,start1_3=?,stop1_3=?,u1_3=?,i1_3=?,start1_4=?,stop1_4=?,u1_4=?,i1_4=?"
    elif dt == "delete2":
        if option == 1:
            plcS7_1200.mbwrite_bool(3,1,3,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(3,1,3,False)
            time.sleep(0.5)
        elif option == 2:
            logotime2(val)
        datamanage.fl_time2 = 1
        sql = "UPDATE time2 SET start2_1=?,stop2_1=?,u2_1=?,i2_1=?,start2_2=?,stop2_2=?,u2_2=?,i2_2=?,start2_3=?,stop2_3=?,u2_3=?,i2_3=?,start2_4=?,stop2_4=?,u2_4=?,i2_4=?"
    elif dt == "delete3":
        if option == 1:
            plcS7_1200.mbwrite_bool(3,1,4,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(3,1,4,False)
            time.sleep(0.5)
        elif option == 2:
            logotime3(val)
        datamanage.fl_time3 = 1
        sql = "UPDATE time3 SET start3_1=?,stop3_1=?,u3_1=?,i3_1=?,start3_2=?,stop3_2=?,u3_2=?,i3_2=?,start3_3=?,stop3_3=?,u3_3=?,i3_3=?,start3_4=?,stop3_4=?,u3_4=?,i3_4=?"
    elif dt == "delete4":
        if option == 1:
            plcS7_1200.mbwrite_bool(3,1,5,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(3,1,5,False)
            time.sleep(0.5)
        elif option == 2:
            logotime4(val)
        datamanage.fl_time4 = 1
        sql = "UPDATE time4 SET start4_1=?,stop4_1=?,u4_1=?,i4_1=?,start4_2=?,stop4_2=?,u4_2=?,i4_2=?,start4_3=?,stop4_3=?,u4_3=?,i4_3=?,start4_4=?,stop4_4=?,u4_4=?,i4_4=?"
    updatedata.sqlupdate(sql,val)

def copy1(dt):
    option = checkoption()
    if datastatus.permission == 1:
        if (dt == 'copy1_2'):
            time1 = updatedata.getsql("select * from time2")
            if option == 1:
                plcS7_1200.mbwrite_bool(3,1,6,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(3,1,6,False)
                time.sleep(0.5)
            elif option == 2:
                logotime1(time1)
            datamanage.fl_time1 = 1
        elif (dt == 'copy1_3'):
            time1 = updatedata.getsql("select * from time3")
            if option == 1:
                plcS7_1200.mbwrite_bool(3,1,7,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(3,1,7,False)
                time.sleep(0.5)
            elif option == 2:
                logotime1(time1)
            datamanage.fl_time1 = 1
        elif (dt == 'copy1_4'):
            time1 = updatedata.getsql("select * from time4")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,0,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,0,False)
                time.sleep(0.5)
            elif option == 2:
                logotime1(time1)
            datamanage.fl_time1 = 1
        sql = "UPDATE time1 SET start1_1=?,stop1_1=?,u1_1=?,i1_1=?,start1_2=?,stop1_2=?,u1_2=?,i1_2=?,start1_3=?,stop1_3=?,u1_3=?,i1_3=?,start1_4=?,stop1_4=?,u1_4=?,i1_4=?"
        updatedata.sqlupdate(sql,time1)
    
def copy2(dt):
    option = checkoption()
    if datastatus.permission == 1:
        if dt == 'copy2_1':
            time2 = updatedata.getsql("select * from time1")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,1,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,1,False)
                time.sleep(0.5)
            elif option == 2:
                logotime2(time2)
            datamanage.fl_time2 = 1
        elif dt == 'copy2_3':
            time2 = updatedata.getsql("select * from time3")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,2,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,2,False)
                time.sleep(0.5)
            elif option == 2:
                logotime2(time2)
            datamanage.fl_time2 = 1
        elif dt == 'copy2_4':
            time2 = updatedata.getsql("select * from time4")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,3,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,3,False)
                time.sleep(0.5)
            elif option == 2:
                logotime2(time2)
            datamanage.fl_time2 = 1
        sql = "UPDATE time2 SET start2_1=?,stop2_1=?,u2_1=?,i2_1=?,start2_2=?,stop2_2=?,u2_2=?,i2_2=?,start2_3=?,stop2_3=?,u2_3=?,i2_3=?,start2_4=?,stop2_4=?,u2_4=?,i2_4=?"
        updatedata.sqlupdate(sql,time2)
    
def copy3(dt):
    option = checkoption()
    if datastatus.permission == 1:
        if dt == 'copy3_1':
            time3 = updatedata.getsql("select * from time1")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,4,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,4,False)
                time.sleep(0.5)
            elif option == 2:
                logotime3(time3)
            datamanage.fl_time3 = 1
        elif dt == 'copy3_2':
            time3 = updatedata.getsql("select * from time2")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,5,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,5,False)
                time.sleep(0.5)
            elif option == 2:
                logotime3(time3)
            datamanage.fl_time3 = 1
        elif dt == 'copy3_4':
            time3 = updatedata.getsql("select * from time4")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,6,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,6,False)
                time.sleep(0.5)
            elif option == 2:
                logotime3(time3)
            datamanage.fl_time3 = 1
        sql = "UPDATE time3 SET start3_1=?,stop3_1=?,u3_1=?,i3_1=?,start3_2=?,stop3_2=?,u3_2=?,i3_2=?,start3_3=?,stop3_3=?,u3_3=?,i3_3=?,start3_4=?,stop3_4=?,u3_4=?,i3_4=?"
        updatedata.sqlupdate(sql,time3)

def copy4(dt):
    option = checkoption()
    if datastatus.permission == 1:
        if dt == 'copy4_1':
            time4 = updatedata.getsql("select * from time1")
            if option == 1:
                plcS7_1200.mbwrite_bool(4,1,7,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(4,1,7,False)
                time.sleep(0.5)
            elif option == 2:
                logotime4(time4)
            datamanage.fl_time4 = 1
        elif dt == 'copy4_2':
            time4 = updatedata.getsql("select * from time2")
            if option == 1:
                plcS7_1200.mbwrite_bool(5,1,0,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(5,1,0,False)
                time.sleep(0.5)
            elif option == 2:
                logotime4(time4)
            datamanage.fl_time4 = 1
        elif dt == 'copy4_3':
            time4 = updatedata.getsql("select * from time3")
            if option == 1:
                plcS7_1200.mbwrite_bool(5,1,1,True)
                time.sleep(0.2)
                plcS7_1200.mbwrite_bool(5,1,1,False)
                time.sleep(0.5)
            elif option == 2:
                logotime4(time4)
            datamanage.fl_time4 = 1
        sql = "UPDATE time4 SET start4_1=?,stop4_1=?,u4_1=?,i4_1=?,start4_2=?,stop4_2=?,u4_2=?,i4_2=?,start4_3=?,stop4_3=?,u4_3=?,i4_3=?,start4_4=?,stop4_4=?,u4_4=?,i4_4=?"
        updatedata.sqlupdate(sql,time4)

def logotime1(time):
    shiftdt_Logo("VW0",time[0].replace(":",""))
    shiftdt_Logo("VW2",time[1].replace(":",""))
    shiftdt_Logo("VW4",time[4].replace(":",""))
    shiftdt_Logo("VW6",time[5].replace(":",""))
    shiftdt_Logo("VW8",time[8].replace(":",""))
    shiftdt_Logo("VW10",time[9].replace(":",""))
    shiftdt_Logo("VW12",time[12].replace(":",""))
    shiftdt_Logo("VW14",time[13].replace(":",""))
def logotime2(time):
    shiftdt_Logo("VW16",time[0].replace(":",""))
    shiftdt_Logo("VW18",time[1].replace(":",""))
    shiftdt_Logo("VW20",time[4].replace(":",""))
    shiftdt_Logo("VW22",time[5].replace(":",""))
    shiftdt_Logo("VW24",time[8].replace(":",""))
    shiftdt_Logo("VW26",time[9].replace(":",""))
    shiftdt_Logo("VW28",time[12].replace(":",""))
    shiftdt_Logo("VW30",time[13].replace(":",""))
def logotime3(time):
    shiftdt_Logo("VW32",time[0].replace(":",""))
    shiftdt_Logo("VW34",time[1].replace(":",""))
    shiftdt_Logo("VW36",time[4].replace(":",""))
    shiftdt_Logo("VW38",time[5].replace(":",""))
    shiftdt_Logo("VW40",time[8].replace(":",""))
    shiftdt_Logo("VW42",time[9].replace(":",""))
    shiftdt_Logo("VW44",time[12].replace(":",""))
    shiftdt_Logo("VW46",time[13].replace(":",""))
def logotime4(time):
    shiftdt_Logo("VW48",time[0].replace(":",""))
    shiftdt_Logo("VW50",time[1].replace(":",""))
    shiftdt_Logo("VW52",time[4].replace(":",""))
    shiftdt_Logo("VW54",time[5].replace(":",""))
    shiftdt_Logo("VW56",time[8].replace(":",""))
    shiftdt_Logo("VW58",time[9].replace(":",""))
    shiftdt_Logo("VW60",time[12].replace(":",""))
    shiftdt_Logo("VW62",time[13].replace(":",""))
def shiftdt_Logo(ad,dt):
    print(dt)
    value = 0
    datasend.temp=0
    for i in range(4):
        value = int(dt)%10
        datasend.temp = datasend.temp + value*pow(16,i)
        dt = int(dt)/10
    print(datasend.temp)
    connect_plcLogo.send_datatoPLC(ad,datasend.temp)

def shiftdt_S71200(num,sta,dt):
    print(dt)
    #plcS7_1200.connect("192.168.8.173",0,1)
    plcS7_1200.dbwrite_byte(num, sta, dt)
    #plcS7_1200.disconnect()

def manual1st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.manual1(dt['m1'])
        option = checkoption()
        if option == 1:
            if int(dt['m1'])==1:
                plcS7_1200.mbwrite_bool(2,1,1,True)
            else:
                plcS7_1200.mbwrite_bool(2,1,1,False)
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time1")
            connect_plcLogo.send_datatoPLC("V1104.0",int(dt['m1']))
            # if datastatus.count1 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]):
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW0",0)
            #             shiftdt_Logo("VW2",0)
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW0",0)
            #             shiftdt_Logo("VW2",0)
            #     else:
            shiftdt_Logo("VW0",0)
            shiftdt_Logo("VW2",0)
            # if datastatus.count1 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW4",0)
            #             shiftdt_Logo("VW6",0)
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW4",0)
            #             shiftdt_Logo("VW6",0)  
            #     else:
            shiftdt_Logo("VW4",0)
            shiftdt_Logo("VW6",0)
            # if datastatus.count1 == 2:   
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW8",0)
            #             shiftdt_Logo("VW10",0)
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW8",0)
            #             shiftdt_Logo("VW10",0)
            #     else:
            shiftdt_Logo("VW8",0)
            shiftdt_Logo("VW10",0)
            # if datastatus.count1 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW12",0)
            #             shiftdt_Logo("VW14",0) 
            #     elif int(time1[12][:2]) > int(time1[13][:2]):
            #         if hour >= time1[12][:2] or hour <= time1[13][:2]:
            #             shiftdt_Logo("VW12",0)
            #             shiftdt_Logo("VW14",0)
            #     else:
            shiftdt_Logo("VW12",0)
            shiftdt_Logo("VW14",0)
            datamanage.fl_manage = 1
            datastatus.manual1 = int(dt['m1'])
        #plcS7_1200.disconnect()
        print('manual1st:', dt['m1'])

def manual2st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.manual2(dt['m2'])
        option = checkoption()
        #plcS7_1200.connect("192.168.8.173",0,1)
        if option == 1:
            if int(dt['m2']) == 1:
                plcS7_1200.mbwrite_bool(2,1,2,True)
            else:
                plcS7_1200.mbwrite_bool(2,1,2,False)
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time2 = updatedata.getsql("select * from time2")
            connect_plcLogo.send_datatoPLC("V1104.1",int(dt['m2']))
            # if datastatus.count2 == 0:
            #     if int(time2[0][:2]) < int(time2[1][:2]):
            #         if (hour >= time2[0][:2] and hour <= time2[1][:2]):
            #             shiftdt_Logo("VW16",0)
            #             shiftdt_Logo("VW18",0)
            #     elif int(time2[0][:2]) > int(time2[1][:2]):
            #         if (hour >= time2[0][:2] or hour <= time2[1][:2]):
            #             shiftdt_Logo("VW16",0)
            #             shiftdt_Logo("VW18",0)
            #     else:
            shiftdt_Logo("VW16",0)
            shiftdt_Logo("VW18",0)
            # elif datastatus.count2 == 1:
            #     if time2[4][:2] < time2[5][:2]:
            #         if (hour >= time2[4][:2] and hour <= time2[5][:2]):
            #             shiftdt_Logo("VW20",0)
            #             shiftdt_Logo("VW22",0)
            #     elif time2[4][:2] > time2[5][:2]:
            #         if (hour >= time2[4][:2] or hour <= time2[5][:2]):
            #             shiftdt_Logo("VW20",0)
            #             shiftdt_Logo("VW22",0)
            #     else:
            shiftdt_Logo("VW20",0)
            shiftdt_Logo("VW22",0)
            # elif datastatus.count2 == 2:
            #     if time2[8][:2] < time2[9][:2]:
            #         if (hour >= time2[8][:2] and hour <= time2[9][:2]):
            #             shiftdt_Logo("VW24",0)
            #             shiftdt_Logo("VW26",0)
            #     elif time2[8][:2] > time2[9][:2]:
            #         if (hour >= time2[8][:2] or hour <= time2[9][:2]):
            #             shiftdt_Logo("VW24",0)
            #             shiftdt_Logo("VW26",0)
            #     else:
            shiftdt_Logo("VW24",0)
            shiftdt_Logo("VW26",0)
            # elif datastatus.count2 == 3:
            #     if time2[12][:2] < time2[13][:2]:
            #         if (hour >= time2[12][:2] and hour <= time2[13][:2]):
            #             shiftdt_Logo("VW28",0)
            #             shiftdt_Logo("VW30",0)
            #     elif time2[12][:2] > time2[13][:2]:
            #         if (hour >= time2[12][:2] or hour <= time2[13][:2]):
            #             shiftdt_Logo("VW28",0)
            #             shiftdt_Logo("VW30",0)
            #     else:
            shiftdt_Logo("VW28",0)
            shiftdt_Logo("VW30",0)
            datamanage.fl_manage = 1
            datastatus.manual2 = int(dt['m2'])
        #plcS7_1200.disconnect()
        print('manual2st:', dt['m2'])

def manual3st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.manual3(dt['m3'])
        option = checkoption()
        '''connect_plcLogo.connect()
        connect_plcLogo.disconnect()'''
        #plcS7_1200.connect("192.168.8.173",0,1)
        if option == 1:
            if int(dt['m3']) == 1:
                plcS7_1200.mbwrite_bool(2,1,3,True)
            else:
                plcS7_1200.mbwrite_bool(2,1,3,False)
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time3")
            connect_plcLogo.send_datatoPLC("V1104.2",int(dt['m3']))
            # if datastatus.count3 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]):
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW32",0)
            #             shiftdt_Logo("VW34",0)
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW32",0)
            #             shiftdt_Logo("VW34",0)
            #     else:
            shiftdt_Logo("VW32",0)
            shiftdt_Logo("VW34",0)
            # if datastatus.count3 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW36",0)
            #             shiftdt_Logo("VW38",0)
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] or hour <= time1[5][:2]:
            #             shiftdt_Logo("VW36",0)
            #             shiftdt_Logo("VW38",0)
            #     else:
            shiftdt_Logo("VW36",0)
            shiftdt_Logo("VW38",0)
            # if datastatus.count3 == 2:
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW40",0)
            #             shiftdt_Logo("VW42",0)
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW40",0)
            #             shiftdt_Logo("VW42",0)
            #     else:
            shiftdt_Logo("VW40",0)
            shiftdt_Logo("VW42",0)
            # if datastatus.count3 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW44",0)
            #             shiftdt_Logo("VW46",0)
            #     elif int(time1[12][:2]) > int(time1[13][:2]):
            #         if hour >= time1[12][:2] or hour <= time1[13][:2]:
            #             shiftdt_Logo("VW44",0)
            #             shiftdt_Logo("VW46",0)
            #     else:
            shiftdt_Logo("VW44",0)
            shiftdt_Logo("VW46",0)
            datamanage.fl_manage = 1
            datastatus.manual3 = int(dt['m3'])
        print('manual3st:', dt['m3'])

def manual4st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.manual4(dt['m4'])
        option = checkoption()
        if option == 1:
            if int(dt['m4']) == 1:
                plcS7_1200.mbwrite_bool(2,1,4,True)
            else:
                plcS7_1200.mbwrite_bool(2,1,4,False)
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time4")
            connect_plcLogo.send_datatoPLC("V1104.3",int(dt['m4']))
            # if datastatus.count4 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]):
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW48",0)
            #             shiftdt_Logo("VW50",0)
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW48",0)
            #             shiftdt_Logo("VW50",0)
            #     else:
            shiftdt_Logo("VW48",0)
            shiftdt_Logo("VW50",0)
            # elif datastatus.count4 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW52",0)
            #             shiftdt_Logo("VW54",0)
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] or hour <= time1[5][:2]:
            #             shiftdt_Logo("VW52",0)
            #             shiftdt_Logo("VW54",0)
            #     else:
            shiftdt_Logo("VW52",0)
            shiftdt_Logo("VW54",0)
            # elif datastatus.count4 == 2:
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW56",0)
            #             shiftdt_Logo("VW58",0)
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW56",0)
            #             shiftdt_Logo("VW58",0)
            #     else:
            shiftdt_Logo("VW56",0)
            shiftdt_Logo("VW58",0)
            # elif datastatus.count4 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW60",0)
            #             shiftdt_Logo("VW62",0)
            #     elif int(time1[12][:2]) > int(time1[13][:2]):
            #         if hour >= time1[12][:2] or hour <= time1[13][:2]:
            #             shiftdt_Logo("VW60",0)
            #             shiftdt_Logo("VW62",0)
            #     else:
            shiftdt_Logo("VW60",0)
            shiftdt_Logo("VW62",0)
            datamanage.fl_manage = 1
            datastatus.manual4 = int(dt['m4'])
        print('manual4st:', dt['m4'])

def auto1st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.auto1(dt['a1'])
        option = checkoption()
        if option == 1:
            plcS7_1200.mbwrite_bool(5,1,3,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(5,1,3,False)
            time.sleep(0.1)
            datamanage.fl_manage = 1
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time1")
            # if datastatus.count1 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]):
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW0",time1[0].replace(":",""))
            #             shiftdt_Logo("VW2",time1[1].replace(":",""))
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW0",time1[0].replace(":",""))
            #             shiftdt_Logo("VW2",time1[1].replace(":",""))
            #     else:
            shiftdt_Logo("VW0",time1[0].replace(":",""))
            shiftdt_Logo("VW2",time1[1].replace(":",""))
            # elif datastatus.count1 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW4",time1[4].replace(":",""))
            #             shiftdt_Logo("VW6",time1[5].replace(":",""))
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] or hour <= time1[5][:2]:
            #             shiftdt_Logo("VW4",time1[4].replace(":",""))
            #             shiftdt_Logo("VW6",time1[5].replace(":",""))
            #     else:
            shiftdt_Logo("VW4",time1[4].replace(":",""))
            shiftdt_Logo("VW6",time1[5].replace(":",""))
            # elif datastatus.count1 == 2:
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW8",time1[8].replace(":",""))
            #             shiftdt_Logo("VW10",time1[9].replace(":",""))
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW8",time1[8].replace(":",""))
            #             shiftdt_Logo("VW10",time1[9].replace(":",""))
            #     else:
            shiftdt_Logo("VW8",time1[8].replace(":",""))
            shiftdt_Logo("VW10",time1[9].replace(":",""))
            # elif datastatus.count1 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW12",time1[12].replace(":",""))
            #             shiftdt_Logo("VW14",time1[13].replace(":","")) 
            #     elif int(time1[12][:2]) > int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW12",time1[12].replace(":",""))
            #             shiftdt_Logo("VW14",time1[13].replace(":",""))
            #     else:
            shiftdt_Logo("VW12",time1[12].replace(":",""))
            shiftdt_Logo("VW14",time1[13].replace(":",""))
            connect_plcLogo.send_datatoPLC("V1104.0",0) 
            datamanage.fl_manage = 1
        print('auto1st:', dt['a1'])

def auto2st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.auto2(dt['a2'])
        option = checkoption()
        if option == 1:
            plcS7_1200.mbwrite_bool(5,1,5,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(5,1,5,False)
            datamanage.fl_manage = 1
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time2 = updatedata.getsql("select * from time2")
            # if datastatus.count2 == 0:
            #     if int(time2[0][:2]) < int(time2[1][:2]):
            #         if (hour >= time2[0][:2] and hour <= time2[1][:2]):
            #             shiftdt_Logo("VW16",time2[0].replace(":",""))
            #             shiftdt_Logo("VW18",time2[1].replace(":",""))
            #     elif int(time2[0][:2]) > int(time2[1][:2]):
            #         if (hour >= time2[0][:2] or hour <= time2[1][:2]):
            #             shiftdt_Logo("VW16",time2[0].replace(":",""))
            #             shiftdt_Logo("VW18",time2[1].replace(":",""))
            #     else:
            shiftdt_Logo("VW16",time2[0].replace(":",""))
            shiftdt_Logo("VW18",time2[1].replace(":",""))
            # elif datastatus.count2 == 1: 
            #     if int(time2[4][:2]) < int(time2[5][:2]):
            #         if (hour >= time2[4][:2] and hour <= time2[5][:2]):
            #             shiftdt_Logo("VW20",time2[4].replace(":",""))
            #             shiftdt_Logo("VW22",time2[5].replace(":",""))
            #     elif int(time2[4][:2]) > int(time2[5][:2]):
            #         if (hour >= time2[4][:2] or hour <= time2[5][:2]):
            #             shiftdt_Logo("VW20",time2[4].replace(":",""))
            #             shiftdt_Logo("VW22",time2[5].replace(":",""))
            #     else:
            shiftdt_Logo("VW20",time2[4].replace(":",""))
            shiftdt_Logo("VW22",time2[5].replace(":",""))
            # elif datastatus.count2 == 2:
            #     if int(time2[8][:2]) < int(time2[9][:2]):
            #         if (hour >= time2[8][:2] and hour <= time2[9][:2]):
            #             shiftdt_Logo("VW24",time2[8].replace(":",""))
            #             shiftdt_Logo("VW26",time2[9].replace(":",""))
            #     elif int(time2[8][:2]) > int(time2[9][:2]):
            #         if (hour >= time2[8][:2] or hour <= time2[9][:2]):
            #             shiftdt_Logo("VW24",time2[8].replace(":",""))
            #             shiftdt_Logo("VW26",time2[9].replace(":",""))
            #     else:
            shiftdt_Logo("VW24",time2[8].replace(":",""))
            shiftdt_Logo("VW26",time2[9].replace(":",""))
            # elif datastatus.count2 == 3:
            #     if int(time2[12][:2]) < int(time2[13][:2]):
            #         if (hour >= time2[12][:2] and hour <= time2[13][:2]):
            #             shiftdt_Logo("VW28",time2[12].replace(":",""))
            #             shiftdt_Logo("VW30",time2[13].replace(":",""))
            #     elif int(time2[12][:2]) > int(time2[13][:2]):
            #         if (hour >= time2[12][:2] or hour <= time2[13][:2]):
            #             shiftdt_Logo("VW28",time2[12].replace(":",""))
            #             shiftdt_Logo("VW30",time2[13].replace(":",""))
            #     else:
            shiftdt_Logo("VW28",time2[12].replace(":",""))
            shiftdt_Logo("VW30",time2[13].replace(":",""))
            connect_plcLogo.send_datatoPLC("V1104.1",0)
            datamanage.fl_manage = 1
        print('auto2st:', dt['a2'])

def auto3st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.auto3(dt['a3'])
        option = checkoption()
        #plcS7_1200.connect("192.168.8.173",0,1)
        if option == 1:
            plcS7_1200.mbwrite_bool(5,1,7,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(5,1,7,False)
            datamanage.fl_manage = 1
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time3")
            # if datastatus.count3 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]): 
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW32",time1[0].replace(":",""))
            #             shiftdt_Logo("VW34",time1[1].replace(":",""))
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW32",time1[0].replace(":",""))
            #             shiftdt_Logo("VW34",time1[1].replace(":",""))
            #     else:
            shiftdt_Logo("VW32",time1[0].replace(":",""))
            shiftdt_Logo("VW34",time1[1].replace(":",""))
            # elif datastatus.count3 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW36",time1[4].replace(":",""))
            #             shiftdt_Logo("VW38",time1[5].replace(":",""))
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] or hour <= time1[5][:2]:
            #             shiftdt_Logo("VW36",time1[4].replace(":",""))
            #             shiftdt_Logo("VW38",time1[5].replace(":",""))
            #     else:
            shiftdt_Logo("VW36",time1[4].replace(":",""))
            shiftdt_Logo("VW38",time1[5].replace(":",""))
            # elif datastatus.count3 == 2:
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW40",time1[8].replace(":",""))
            #             shiftdt_Logo("VW42",time1[9].replace(":",""))
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW40",time1[8].replace(":",""))
            #             shiftdt_Logo("VW42",time1[9].replace(":",""))
            #     else:
            shiftdt_Logo("VW40",time1[8].replace(":",""))
            shiftdt_Logo("VW42",time1[9].replace(":",""))
            # elif datastatus.count3 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW44",time1[12].replace(":",""))
            #             shiftdt_Logo("VW46",time1[13].replace(":",""))
            #     elif int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] or hour <= time1[13][:2]:
            #             shiftdt_Logo("VW44",time1[12].replace(":",""))
            #             shiftdt_Logo("VW46",time1[13].replace(":",""))
            #     else:
            shiftdt_Logo("VW44",time1[12].replace(":",""))
            shiftdt_Logo("VW46",time1[13].replace(":",""))
            datamanage.fl_manage = 1
            connect_plcLogo.send_datatoPLC("V1104.2",0)
        #plcS7_1200.disconnect()
        print('auto3st:', dt['a3'])

def auto4st(dt):
    if datastatus.permission == 1 or datastatus.server_control == 1:
        updatedata.auto4(dt['a4'])
        option = checkoption()
        #plcS7_1200.connect("192.168.8.173",0,1)
        if option == 1:
            plcS7_1200.mbwrite_bool(6,1,1,True)
            time.sleep(0.2)
            plcS7_1200.mbwrite_bool(6,1,1,False)
            datamanage.fl_manage = 1
        elif option == 2:
            hour = (datetime.now()).strftime('%H')
            time1 = updatedata.getsql("select * from time4")
            # if datastatus.count4 == 0:
            #     if int(time1[0][:2]) < int(time1[1][:2]):
            #         if hour >= time1[0][:2] and hour <= time1[1][:2]:
            #             shiftdt_Logo("VW48",time1[0].replace(":",""))
            #             shiftdt_Logo("VW50",time1[1].replace(":",""))
            #     elif int(time1[0][:2]) > int(time1[1][:2]):
            #         if hour >= time1[0][:2] or hour <= time1[1][:2]:
            #             shiftdt_Logo("VW48",time1[0].replace(":",""))
            #             shiftdt_Logo("VW50",time1[1].replace(":",""))
            #     else:
            shiftdt_Logo("VW48",time1[0].replace(":",""))
            shiftdt_Logo("VW50",time1[1].replace(":",""))
            # elif datastatus.count4 == 1:
            #     if int(time1[4][:2]) < int(time1[5][:2]):
            #         if hour >= time1[4][:2] and hour <= time1[5][:2]:
            #             shiftdt_Logo("VW52",time1[4].replace(":",""))
            #             shiftdt_Logo("VW54",time1[5].replace(":",""))
            #     elif int(time1[4][:2]) > int(time1[5][:2]):
            #         if hour >= time1[4][:2] or hour <= time1[5][:2]:
            #             shiftdt_Logo("VW52",time1[4].replace(":",""))
            #             shiftdt_Logo("VW54",time1[5].replace(":",""))
            #     else:
            shiftdt_Logo("VW52",time1[4].replace(":",""))
            shiftdt_Logo("VW54",time1[5].replace(":",""))
            # elif datastatus.count4 == 2:
            #     if int(time1[8][:2]) < int(time1[9][:2]):
            #         if hour >= time1[8][:2] and hour <= time1[9][:2]:
            #             shiftdt_Logo("VW56",time1[8].replace(":",""))
            #             shiftdt_Logo("VW58",time1[9].replace(":",""))
            #     elif int(time1[8][:2]) > int(time1[9][:2]):
            #         if hour >= time1[8][:2] or hour <= time1[9][:2]:
            #             shiftdt_Logo("VW56",time1[8].replace(":",""))
            #             shiftdt_Logo("VW58",time1[9].replace(":",""))
            #     else:
            shiftdt_Logo("VW56",time1[8].replace(":",""))
            shiftdt_Logo("VW58",time1[9].replace(":",""))
            # elif datastatus.count4 == 3:
            #     if int(time1[12][:2]) < int(time1[13][:2]):
            #         if hour >= time1[12][:2] and hour <= time1[13][:2]:
            #             shiftdt_Logo("VW60",time1[12].replace(":",""))
            #             shiftdt_Logo("VW62",time1[13].replace(":",""))
            #     elif int(time1[12][:2]) > int(time1[13][:2]):
            #         if hour >= time1[12][:2] or hour <= time1[13][:2]:
            #             shiftdt_Logo("VW60",time1[12].replace(":",""))
            #             shiftdt_Logo("VW62",time1[13].replace(":",""))
            #     else:
            shiftdt_Logo("VW60",time1[12].replace(":",""))
            shiftdt_Logo("VW62",time1[13].replace(":",""))
            datamanage.fl_manage = 1
            connect_plcLogo.send_datatoPLC("V1104.3",0)
        print('auto4st:', dt['a4'])
#######################

def manage(dt):
    datamanage.fl_manage = 1
    updatedata.updatemanage(dt['id'], dt['manager'], dt['lightbranch'])
    print(dt['id'], dt['manager'], dt['lightbranch'])

def refresh(dt):
    if (dt == "refreshhomepage"):
        datamanage.fl_manage = 1
        datamanage.fl_time = 1
    elif (dt == "refreshsettinghome"):
        datamanage.fl_setting = 1
    elif (dt == "refreshsetting1"):
        datamanage.fl_time1 = 1
    elif (dt == "refreshsetting2"):
        datamanage.fl_time2 = 1
    elif (dt == "refreshsetting3"):
        datamanage.fl_time3 = 1
    elif (dt == "refreshsetting4"):
        datamanage.fl_time4 = 1
    elif (dt == "refreshsystem"):
        datamanage.fl_system = 1