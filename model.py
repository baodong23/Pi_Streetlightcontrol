class js_manage(object):
    def __init__(self):
        self.jsid = 0
        self.jsmanager = 0
        self.jslightbranch = 0
    
    def __str__(self):
        s = '{{"jsid" : "{0}", "jsmanager" : "{1}", "jslightbranch" : "{2}"}}'
        return s.format(self.jsid, self.jsmanager, self.jslightbranch)

class js_status(object):
    def __init__(self):
        self.jsmanual1 = 0
        self.jsmanual2 = 0
        self.jsmanual3 = 0
        self.jsmanual4 = 0
        self.jsauto1 = 0
        self.jsauto2 = 0 
        self.jsauto3 = 0
        self.jsauto4 = 0
    
    def __str__(self):
        s = '{{"jsmanual1" : "{0}", "jsmanual2" : "{1}", "jsmanual3" : "{2}", "jsmanual4" : "{3}", "jsauto1" : "{4}", "jsauto2" : "{5}", "jsauto3" : "{6}", "jsauto4" : "{7}"}}'
        return s.format(self.jsmanual1,self.jsmanual2,self.jsmanual3,self.jsmanual4,self.jsauto1,self.jsauto2,self.jsauto3,self.jsauto4)

class js_timecontrol1(object):
    def __init__(self):
        self.starttime1_1 = 0
        self.stoptime1_1 = 0
        self.u1_1max = 0
        self.i1_1max = 0
        self.starttime1_2 = 0
        self.stoptime1_2 = 0
        self.u1_2max = 0
        self.i1_2max = 0
        self.starttime1_3 = 0
        self.stoptime1_3 = 0
        self.u1_3max = 0
        self.i1_3max = 0
        self.starttime1_4 = 0
        self.stoptime1_4 = 0
        self.u1_4max = 0
        self.i1_4max = 0

    def __str__(self):
        s = '{{"starttime1_1":"{0}","stoptime1_1":"{1}","u1_1max":"{2}","i1_1max":"{3}","starttime1_2":"{4}","stoptime1_2":"{5}","u1_2max":"{6}","i1_2max":"{7}","starttime1_3":"{8}","stoptime1_3":"{9}","u1_3max":"{10}","i1_3max":"{11}","starttime1_4":"{12}","stoptime1_4":"{13}","u1_4max":"{14}","i1_4max":"{15}"}}'   
        return s.format(self.starttime1_1,self.stoptime1_1,self.u1_1max,self.i1_1max,self.starttime1_2,self.stoptime1_2,self.u1_2max,self.i1_2max,self.starttime1_3,self.stoptime1_3,self.u1_3max,self.i1_3max,self.starttime1_4,self.stoptime1_4,self.u1_4max,self.i1_4max)

class js_timecontrol2(object):
    def __init__(self):
        self.starttime2_1 = 0
        self.stoptime2_1 = 0
        self.u2_1max = 0
        self.i2_1max = 0
        self.starttime2_2 = 0
        self.stoptime2_2 = 0
        self.u2_2max = 0
        self.i2_2max = 0
        self.starttime2_3 = 0
        self.stoptime2_3 = 0
        self.u2_3max = 0
        self.i2_3max = 0
        self.starttime2_4 = 0
        self.stoptime2_4 = 0
        self.u2_4max = 0
        self.i2_4max = 0

    def __str__(self):
        s = '{{"starttime2_1":"{0}","stoptime2_1":"{1}","u2_1max":"{2}","i2_1max":"{3}","starttime2_2":"{4}","stoptime2_2":"{5}","u2_2max":"{6}","i2_2max":"{7}","starttime2_3":"{8}","stoptime2_3":"{9}","u2_3max":"{10}","i2_3max":"{11}","starttime2_4":"{12}","stoptime2_4":"{13}","u2_4max":"{14}","i2_4max":"{15}"}}'   
        return s.format(self.starttime2_1,self.stoptime2_1,self.u2_1max,self.i2_1max,self.starttime2_2,self.stoptime2_2,self.u2_2max,self.i2_2max,self.starttime2_3,self.stoptime2_3,self.u2_3max,self.i2_3max,self.starttime2_4,self.stoptime2_4,self.u2_4max,self.i2_4max)

class js_timecontrol3(object):
    def __init__(self):
        self.starttime3_1 = 0
        self.stoptime3_1 = 0
        self.u3_1max = 0
        self.i3_1max = 0
        self.starttime3_2 = 0
        self.stoptime3_2 = 0
        self.u3_2max = 0
        self.i3_2max = 0
        self.starttime3_3 = 0
        self.stoptime3_3 = 0
        self.u3_3max = 0
        self.i3_3max = 0
        self.starttime3_4 = 0
        self.stoptime3_4 = 0
        self.u3_4max = 0
        self.i3_4max = 0

    def __str__(self):
        s = '{{"starttime3_1":"{0}","stoptime3_1":"{1}","u3_1max":"{2}","i3_1max":"{3}","starttime3_2":"{4}","stoptime3_2":"{5}","u3_2max":"{6}","i3_2max":"{7}","starttime3_3":"{8}","stoptime3_3":"{9}","u3_3max":"{10}","i3_3max":"{11}","starttime3_4":"{12}","stoptime3_4":"{13}","u3_4max":"{14}","i3_4max":"{15}"}}'   
        return s.format(self.starttime3_1,self.stoptime3_1,self.u3_1max,self.i3_1max,self.starttime3_2,self.stoptime3_2,self.u3_2max,self.i3_2max,self.starttime3_3,self.stoptime3_3,self.u3_3max,self.i3_3max,self.starttime3_4,self.stoptime3_4,self.u3_4max,self.i3_4max)

class js_timecontrol4(object):
    def __init__(self):
        self.starttime4_1 = 0
        self.stoptime4_1 = 0
        self.u4_1max = 0
        self.i4_1max = 0
        self.starttime4_2 = 0
        self.stoptime4_2 = 0
        self.u4_2max = 0
        self.i4_2max = 0
        self.starttime4_3 = 0
        self.stoptime4_3 = 0
        self.u4_3max = 0
        self.i4_3max = 0
        self.starttime4_4 = 0
        self.stoptime4_4 = 0
        self.u4_4max = 0
        self.i4_4max = 0

    def __str__(self):
        s = '{{"starttime4_1":"{0}","stoptime4_1":"{1}","u4_1max":"{2}","i4_1max":"{3}","starttime4_2":"{4}","stoptime4_2":"{5}","u4_2max":"{6}","i4_2max":"{7}","starttime4_3":"{8}","stoptime4_3":"{9}","u4_3max":"{10}","i4_3max":"{11}","starttime4_4":"{12}","stoptime4_4":"{13}","u4_4max":"{14}","i4_4max":"{15}"}}'   
        return s.format(self.starttime4_1,self.stoptime4_1,self.u4_1max,self.i4_1max,self.starttime4_2,self.stoptime4_2,self.u4_2max,self.i4_2max,self.starttime4_3,self.stoptime4_3,self.u4_3max,self.i4_3max,self.starttime4_4,self.stoptime4_4,self.u4_4max,self.i4_4max)

class js_MFMpara(object):
    def __init__(self):
        self.vol1 = 0
        self.vol2 = 0
        self.vol3 = 0
        self.cur1 = 0
        self.cur2 = 0
        self.cur3 = 0
        self.pow1 = 0
        self.pow2 = 0
        self.pow3 = 0
        self.aPf = 0
        self.Qc = 0
        self.avol = 0
        self.acur = 0
        self.tpow = 0

    def __str__(self):
        s = '{{"vol1":"{0}","vol2":"{1}","vol3":"{2}","cur1":"{3}","cur2":"{4}","cur3":"{5}","pow1":"{6}","pow2":"{7}","pow3":"{8}","aPf":"{9}","Qc":"{10}","avol":"{11}","acur":"{12}","tpow":"{13}"}}'
        return s.format(self.vol1, self.vol2, self.vol3, self.cur1, self.cur2, self.cur3, self.pow1, self.pow2, self.pow3, self.aPf, self.Qc, self.avol, self.acur, self.tpow)

class js_system(object):
    def __init__(self):
        self.connect_PLC = 0
    
    def __str__(self):
        s = '{{"connect_PLC":"{0}"}}'
        return s.format(self.connect_PLC)
    
class js_login(object):
    def __init__(self):
        self.login = 0
    
    def __str__(self):
        s = '{{"login":"{0}"}}'
        return s.format(self.login)

class js_timehome(object):
    def __init__(self):
        self.starttime = 0
        self.stoptime = 0
    
    def __str__(self):
        s = '{{"starttime":"{0}","stoptime":"{1}"}}'
        return s.format(self.starttime, self.stoptime)

class js_timecontrol(object):
    def __init__(self):
        self.start1 = 0
        self.stop1 = 0
        self.start2 = 0
        self.stop2 = 0
        self.start3 = 0
        self.stop3 = 0
        self.start4 = 0
        self.stop4 = 0

    def __str__(self):
        s = '{{"start1":"{0}","stop1":"{1}","start2":"{2}","stop2":"{3}","start3":"{4}","stop3":"{5}","start4":"{6}","stop4":"{7}"}}'    
        return s.format(self.start1, self.stop1, self.start2, self.stop2, self.start3, self.stop3, self.start4, self.stop4)

class js_settinghome(object):
    def __init__(self):
        self.u1max = 0
        self.u2max = 0
        self.u3max = 0
        self.i1max = 0
        self.i2max = 0
        self.i3max = 0
        self.w1max = 0
        self.w2max = 0
        self.w3max = 0
        self.Pfmax = 0
        self.Irmax = 0
        self.Qcmax = 0
    def __str__(self):
        s = '{{"u1max":"{0}","u2max":"{1}","u3max":"{2}","i1max":"{3}","i2max":"{4}","i3max":"{5}","w1max":"{6}","w2max":"{7}","w3max":"{8}","Pfmax":"{9}","Irmax":"{10}","Qcmax":"{11}"}}'
        return s.format(self.u1max,self.u2max,self.u3max,self.i1max,self.i2max,self.i3max,self.w1max,self.w2max,self.w3max,self.Pfmax,self.Irmax,self.Qcmax)

class js_lightstatus(object):
    def __int__(self):
        self.light1 = 0
        self.light2 = 0
        self.light3 = 0
        self.light4 = 0

    def __str__(self):
        s = '{{"light1": "{0}","light2": "{1}","light3": "{2}","light4": "{3}"}}'
        return s.format(self.light1, self.light2, self.light3, self.light4)
      
class js_btnbranch(object):
    def __init__(self):
        self.btn_branch1 = 0
        self.btn_branch2 = 0
        self.btn_branch3 = 0
        self.btn_branch4 = 0

    def __str__(self):
        s = '{{"btn_branch1" : "{0}", "btn_branch2" : "{1}", "btn_branch3" : "{2}", "btn_branch4" : "{3}"}}'
        return s.format(self.btn_branch1,self.btn_branch2,self.btn_branch3,self.btn_branch4)