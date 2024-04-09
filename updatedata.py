import sqlite3

def sqlupdate(tab,data):
    cnx = sqlite3.connect("/home/bao/amtlight.db")
    mycursor = cnx.cursor()
    mycursor.execute(tab,data)
    cnx.commit()
    cnx.close()
def deletedata(dt):
    cnx = sqlite3.connect("/home/bao/amtlight.db")
    mycursor = cnx.cursor()
    mycursor.execute(dt)
    cnx.close()
def getsql(dt):
    cnx = sqlite3.connect("/home/bao/amtlight.db")
    mycursor = cnx.cursor()
    mycursor.execute(dt)
    data = mycursor.fetchone()
    cnx.close()
    return data
def getall(dt):
    cnx = sqlite3.connect("/home/bao/amtlight.db")
    mycursor = cnx.cursor()
    mycursor.execute(dt)
    data = mycursor.fetchall()
    listdata = list()
    for i in data:
        listdata.append(list(i))
    cnx.close()
    return listdata

def updatedatauser(ip, per):
    sql = "UPDATE datauser SET IP_client=?, permission=?"
    val = (ip, per)
    sqlupdate(sql,val) 
def updatemanage(id,manage,branch):
    sql = "UPDATE cf SET ID=?, manage=?, branch=?"
    val = (id,manage,branch)
    sqlupdate(sql,val)
def updateoption(option, IP):
    sql = "UPDATE cf SET option=?, IP=?"
    val = (option,IP)
    sqlupdate(sql,val)
def updateMFM383A(dt):
    sql = "INSERT INTO MFM383A VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    val = (dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11],dt[12],dt[13],
           dt[14],dt[15],dt[16],dt[17],dt[18],dt[19],dt[20],dt[21],dt[22],dt[23],dt[24],dt[25],
           dt[26],dt[27],dt[28],dt[29],dt[30],dt[31])
    sqlupdate(sql,val)
def manual1(dt):
    sql = "UPDATE status_control SET manual1=?, auto1=?"
    val = (dt,0)
    sqlupdate(sql,val)

def manual2(dt):
    sql = "UPDATE status_control SET manual2=?, auto2=?"
    val = (dt,0)
    sqlupdate(sql,val)

def manual3(dt):
    sql = "UPDATE status_control SET manual3=?, auto3=?"
    val = (dt,0)
    sqlupdate(sql,val)

def manual4(dt):
    sql = "UPDATE status_control SET manual4=?, auto4=?"
    val = (dt,0)
    sqlupdate(sql,val)

def auto1(dt):
    sql = "UPDATE status_control SET auto1=?, manual1=?"
    val = (dt,0)
    sqlupdate(sql,val)

def auto2(dt):
    sql = "UPDATE status_control SET auto2=?, manual2=?"
    val = (dt,0)
    sqlupdate(sql,val)

def auto3(dt):
    sql = "UPDATE status_control SET auto3=?, manual3=?"
    val = (dt,0)
    sqlupdate(sql,val)

def auto4(dt):
    sql = "UPDATE status_control SET auto4=?, manual4=?"
    val = (dt,0)
    sqlupdate(sql,val)