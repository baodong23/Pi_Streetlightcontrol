from web import socketio
import data

@socketio.on('connect')
def connect():
    print('connected')

@socketio.on('disconnect')
def disconnect():
    print('disconnected')
    
@socketio.on('message')
def handle_message(msg):
    data.handle_msg(msg)

def onManage(msg):
    socketio.emit('manage', msg)

def onControl(msg):
    socketio.emit('control', msg)

def ontimehome(msg):
    socketio.emit('timehome', msg)

def ontimeControl(msg):
    socketio.emit('timecontrol', msg)
    
def ontimeControl1(msg):
    socketio.emit('timecontrol1', msg)

def ontimeControl2(msg):
    socketio.emit('timecontrol2', msg)

def ontimeControl3(msg):
    socketio.emit('timecontrol3', msg)

def ontimeControl4(msg):
    socketio.emit('timecontrol4', msg)

def onpara(msg):
    socketio.emit('parameter', msg)

def onerror(msg):
    socketio.emit('error', msg)

def onerrorcode(msg):
    socketio.emit('errorcode', msg)

def onConnect_PLC(msg):
    socketio.emit('get_connect',msg)

def onsettinghome(msg):
    socketio.emit('settinghome', msg)
     
def onsuccess(msg):
    socketio.emit('settinghome', msg)

def onlightstatus(msg):
    socketio.emit('lightstatus', msg)

def onloginok(msg):
    socketio.emit('loginok', msg)
def onlogin(msg):
    socketio.emit('login', msg)
def onip(msg):
    socketio.emit('ip',msg)