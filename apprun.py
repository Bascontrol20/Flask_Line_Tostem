#https://pypi.org/project/threaded/
### WebPage insert data complete, sampling message 1 msg Update 10Nov2021
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_sqlalchemy import SQLAlchemy


import json
import requests
import pymcprotocol #for PLC
import threading
import datetime

#**************CONFIGURATIONS*******************
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Linenotify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#**************DATABASE*******************
class Linenotify(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    linegroup = db.Column(db.String(100))
    linemsg = db.Column(db.String(50))
    linetoken = db.Column(db.String(200))
    lineplc = db.Column(db.String(200))

    # def __repr__(self):
    #     return f"Linenotify('{self.linegroup}','{self.linemsg}','{self.linetoken}')"
    def __init__(self,linegroup,linemsg,linetoken,lineplc):
        self.linegroup = linegroup
        self.linemsg = linemsg
        self.linetoken = linetoken
        self.lineplc = lineplc

#Use for create new database
#db.create_all()

@app.route('/')
def Index():
    all_line = Linenotify.query.all()

    return render_template("index.html", all_lines=all_line)

@app.route('/insert', methods = ['POST'])
def insert():

    linegroup = request.form['groupname']
    linemsg = request.form['linemessage']
    linetoken = request.form['linetoken']
    lineplc = request.form['lineplc']

    my_data = Linenotify(linegroup,linemsg,linetoken,lineplc)
    db.session.add(my_data)
    db.session.commit()

    return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    delete_msg =  Linenotify.query.get(id_data)
    db.session.delete(delete_msg)
    db.session.commit()
    return redirect(url_for('Index'))

@app.route('/update',methods=['POST','GET'])
def update():
    # update_data = Linenotify.query.get(id)
    if request.method == 'POST':

        id = request.form['id']
        update = Linenotify.query.get(id)
        update.linegroup = request.form['groupname']
        update.linemsg = request.form['linemessage']
        update.linetoken = request.form['linetoken']
        update.lineplc = request.form['lineplc']
        #flash("Data Updated Successfully")
        db.session.commit()

    return redirect(url_for('Index'))

#####PLC SECTION###

def plc_notify():
    
    print("PLC notify Running...")
    # Set frame type
    slmp = pymcprotocol.Type3E()
    # Set PLC type
    slmp = pymcprotocol.Type3E(plctype="iQ-R")
    # Connect PLC
    slmp.connect("192.168.1.81", 8880)
    #get_url = "http://127.0.0.1:8000/api/?format=json"
    #resp = requests.get(get_url)
    #line_tokenget = Linenotify.query.filter_by(id=1)
    # line_all = Linenotify.query.all()
    # for line in line_all:
    #     print("Message : ",line.linemsg)
    #     print("Token : ",line.linetoken)

    #print("Message1",line_all.linemsg[0])
    #print("Message2",line_all.linemsg[1])
    

    
    head_device = 'M10000'
    device_batch_read = slmp.batchread_bitunits(headdevice=head_device, readsize=50)

    threading.Timer(5.0,plc_notify).start()
    '''MC01 M10000-M10009'''
    #MessageNo.1 M10000
    if device_batch_read[0] == 1:
        id= Linenotify.query.filter_by(lineplc='M10000')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10000')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.2 M10001
    if device_batch_read[1] == 1:
        id= Linenotify.query.filter_by(lineplc='M10001')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10001')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.3 M10002
    if device_batch_read[2] == 1:
        id= Linenotify.query.filter_by(lineplc='M10002')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10002')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.4 M10003
    if device_batch_read[3] == 1:
        id= Linenotify.query.filter_by(lineplc='M10003')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10003')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.5 M10004
    if device_batch_read[4] == 1:
        id= Linenotify.query.filter_by(lineplc='M10004')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10004')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.6 M10005
    if device_batch_read[5] == 1:
        id= Linenotify.query.filter_by(lineplc='M10005')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10005')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.7 M10006
    if device_batch_read[6] == 1:
        id= Linenotify.query.filter_by(lineplc='M10006')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10006')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.8 M10007
    if device_batch_read[7] == 1:
        id= Linenotify.query.filter_by(lineplc='M10007')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10007')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.9 M10008
    if device_batch_read[8] == 1:
        id= Linenotify.query.filter_by(lineplc='M10008')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10008')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.10 M10009
    if device_batch_read[9] == 1:
        id= Linenotify.query.filter_by(lineplc='M10009')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10009')[0].linemsg
        line_notify(msg1,id)


    '''MC01 M10010-M10019'''
    #MessageNo.11 M10010
    if device_batch_read[10] == 1:
        id= Linenotify.query.filter_by(lineplc='M10010')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10010')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.12 M10011
    if device_batch_read[11] == 1:
        id= Linenotify.query.filter_by(lineplc='M10011')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10011')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.13 M10012
    if device_batch_read[12] == 1:
        id= Linenotify.query.filter_by(lineplc='M10012')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10012')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.14 M10013
    if device_batch_read[13] == 1:
        id= Linenotify.query.filter_by(lineplc='M10013')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10013')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.15 M10014
    if device_batch_read[14] == 1:
        id= Linenotify.query.filter_by(lineplc='M10014')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10014')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.16 M10015
    if device_batch_read[15] == 1:
        id= Linenotify.query.filter_by(lineplc='M10015')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10015')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.17 M10016
    if device_batch_read[16] == 1:
        id= Linenotify.query.filter_by(lineplc='M10016')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10016')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.18 M10017
    if device_batch_read[17] == 1:
        id= Linenotify.query.filter_by(lineplc='M10017')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10017')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.19 M10018
    if device_batch_read[18] == 1:
        id= Linenotify.query.filter_by(lineplc='M10018')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10018')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.20 M10019
    if device_batch_read[19] == 1:
        id= Linenotify.query.filter_by(lineplc='M10019')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10019')[0].linemsg
        line_notify(msg1,id)


    '''MC01 M10020-M10029'''
    #MessageNo.21 M10020
    if device_batch_read[20] == 1:
        id= Linenotify.query.filter_by(lineplc='M10020')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10020')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.22 M10021
    if device_batch_read[21] == 1:
        id= Linenotify.query.filter_by(lineplc='M10021')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10021')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.23 M10022
    if device_batch_read[22] == 1:
        id= Linenotify.query.filter_by(lineplc='M10022')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10022')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.24 M10023
    if device_batch_read[23] == 1:
        id= Linenotify.query.filter_by(lineplc='M10023')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10023')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.25 M10024
    if device_batch_read[24] == 1:
        id= Linenotify.query.filter_by(lineplc='M10024')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10024')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.26 M10025
    if device_batch_read[25] == 1:
        id= Linenotify.query.filter_by(lineplc='M10025')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10025')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.27 M10026
    if device_batch_read[26] == 1:
        id= Linenotify.query.filter_by(lineplc='M10026')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10026')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.28 M10027
    if device_batch_read[27] == 1:
        id= Linenotify.query.filter_by(lineplc='M10027')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10027')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.29 M10028
    if device_batch_read[28] == 1:
        id= Linenotify.query.filter_by(lineplc='M10028')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10028')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.30 M10029
    if device_batch_read[29] == 1:
        id= Linenotify.query.filter_by(lineplc='M10029')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10029')[0].linemsg
        line_notify(msg1,id)

    '''MC01 M10030-M10039'''
    #MessageNo.31 M10030
    if device_batch_read[30] == 1:
        id= Linenotify.query.filter_by(lineplc='M10030')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10030')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.32 M10031
    if device_batch_read[31] == 1:
        id= Linenotify.query.filter_by(lineplc='M10031')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10031')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.33 M10032
    if device_batch_read[32] == 1:
        id= Linenotify.query.filter_by(lineplc='M10032')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10032')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.34 M10033
    if device_batch_read[33] == 1:
        id= Linenotify.query.filter_by(lineplc='M10033')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10033')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.35 M10034
    if device_batch_read[34] == 1:
        id= Linenotify.query.filter_by(lineplc='M10034')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10034')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.36 M10035
    if device_batch_read[35] == 1:
        id= Linenotify.query.filter_by(lineplc='M10035')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10035')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.37 M10036
    if device_batch_read[36] == 1:
        id= Linenotify.query.filter_by(lineplc='M10036')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10036')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.38 M10037
    if device_batch_read[37] == 1:
        id= Linenotify.query.filter_by(lineplc='M10037')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10037')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.39 M10038
    if device_batch_read[38] == 1:
        id= Linenotify.query.filter_by(lineplc='M10038')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10038')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.40 M10039
    if device_batch_read[39] == 1:
        id= Linenotify.query.filter_by(lineplc='M10039')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10039')[0].linemsg
        line_notify(msg1,id)

    '''MC01 M10040-M10049'''
    #MessageNo.41 M10040
    if device_batch_read[40] == 1:
        id= Linenotify.query.filter_by(lineplc='M10040')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10040')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.42 M10041
    if device_batch_read[41] == 1:
        id= Linenotify.query.filter_by(lineplc='M10041')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10041')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.43 M10042
    if device_batch_read[42] == 1:
        id= Linenotify.query.filter_by(lineplc='M10042')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10042')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.44 M10043
    if device_batch_read[43] == 1:
        id= Linenotify.query.filter_by(lineplc='M10043')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10043')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.45 M10044
    if device_batch_read[44] == 1:
        id= Linenotify.query.filter_by(lineplc='M10044')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10044')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.46 M10045
    if device_batch_read[45] == 1:
        id= Linenotify.query.filter_by(lineplc='M10045')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10045')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.47 M10046
    if device_batch_read[46] == 1:
        id= Linenotify.query.filter_by(lineplc='M10046')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10046')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.48 M10047
    if device_batch_read[47] == 1:
        id= Linenotify.query.filter_by(lineplc='M10047')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10047')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.49 M10048
    if device_batch_read[48] == 1:
        id= Linenotify.query.filter_by(lineplc='M10048')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10048')[0].linemsg
        line_notify(msg1,id)
    #MessageNo.50 M10049
    if device_batch_read[49] == 1:
        id= Linenotify.query.filter_by(lineplc='M10049')[0].linetoken
        msg1 = Linenotify.query.filter_by(lineplc='M10049')[0].linemsg
        line_notify(msg1,id)

    

def line_notify(message,id):

    # tokendb = Linemessage.objects.get(id=id).linetoken
    tokendb = id
    #print(tokendb)
    url = 'https://notify-api.line.me/api/notify'
    token1 = tokendb
    headers1 = {'content-type':'application/x-www-form-urlencoded',
                'Authorization':'Bearer '+token1}
    msg1 = message
    r = requests.post(url, headers=headers1 , data = {'message':msg1})

    print(r.text)


if __name__ == '__main__':
    plc_notify()
    app.run(debug=True)