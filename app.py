from flask import Flask,request,render_template
from data import arr
import pickle
app = Flask(__name__)
# for i in arr:
#        print(i)
#        print(i['name'],i['voter'],i['adh'])
@app.route('/')
def hello():
       # return("hello")
      return render_template('login.html')
name_aadhar= ""
v_id=0
a_id=0
@app.route('/form_login',methods=['POST',"GET"])
def login():
        vote = request.form['Voter']
        Aadhar = request.form['Aadhar']
        vote = int(vote)
        Aadhar = int(Aadhar)
        for i in arr:
                print(vote, Aadhar)
                print(i['voter'], i['adh'])
                if i['voter'] == vote and i['adh']==Aadhar:
                        global name_aadhar,v_id,a_id
                        name_aadhar=i['name']
                        v_id = i['voter']
                        a_id = i['adh']
                        return render_template('face_auth.html',name=i['name'])
        else:
             return render_template('login.html', info="Sorry Invalid check your Aadhar and Voter Number")

                # elif i['voter'] == vote and i['adh']!=Aadhar:
                #         return render_template('login.html',info="Invalid Aadhar Number")
                # elif i['voter'] != vote and i['adh']==Aadhar:
                #         return render_template('login.html',info="Invalid Voter Number")
                # elif i['voter'] != vote and i['adh']!=Aadhar:
                #      return render_template('login.html',info="Invalid Aadhar & Voter Number")
print(name_aadhar)
@app.route('/open_me',methods=["POST"])
def open_me():
        import face_faco
        x=face_faco.check_eligible()
        if name_aadhar.lower()==x.lower():
                 return render_template('vote.html',name=name_aadhar,v_id=v_id,a_id=a_id)
        else:
                return render_template('failed.html', info="Sorry Your Authentication Failed")
