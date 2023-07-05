import os
from flask import Flask,render_template
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL


app=Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']="localhost"


@app.route("/indexpage")
def indexpage():
    return render_template("indexpage.html")

@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if username=="admin" and password=="admin":
           return redirect('adminhome')
        else:
            error="invalid"
    else:
        return render_template("adminlogin.html")

@app.route("/adminmailalert")
def adminmailalert():
    return render_template("adminmailalert.html")

@app.route("/adminviewenduser")
def adminviewenduser():
    return render_template("adminviewenduser.html")

@app.route("/adminaddenduser")
def adminaddenduser():
    return render_template("adminaddenduser.html")    

@app.route("/adminviewreport")
def adminviewreport():
    return render_template("adminviewreport.html")

@app.route("/adminviewuser")
def adminviewuser():
    return render_template("adminviewuser.html")

@app.route("/enduserhome")
def enduserhome():
    return render_template("enduserhome.html")

@app.route("/enduserlogin")
def enduserlogin():
    return render_template("enduserlogin.html")

@app.route("/enduserreport")
def enduserreport():
    return render_template("enduserreport.html")

@app.route("/enduserview")
def enduserview():
    return render_template("enduserview.html")

@app.route("/userhome")
def userhome():
    return render_template("userhome.html")

@app.route("/userlogin",methods=['POST','GET'])
def userlogin():
    if request.method=='POST':
        mailid=request.form['mailid']
        password=request.form['password']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("SELECT * FROM `userreg` WHERE 'mailid'='"+mailid+"' AND 'password'='"+password+"'")
        data=cur.fetchone()
        if data[3]==mailid and data[4]==password:
            return redirect(url_for('userhome',id=data[0]))
        else:
            error='invalid'
    else:        
        return render_template("userlogin.html")

@app.route("/userreg",methods=['POST','GET'])
def userreg():
    if request.method=='POST':
        username=request.form['username']
        phonenumber=request.form['phonenumber']
        mailid=request.form['mailid']
        password=request.form['password']
        confirmpassword=request.form['confirmpassword']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `userreg`( `username`, `phonenumber`, `mailid`, `password`, `confirmpassword`) VALUES (%s,%s,%s,%s,%s)",( username, phonenumber, mailid, password, confirmpassword))
        con.commit()
        return redirect('userlogin')
    else:
        return render_template("userreg.html")

@app.route("/userupload")
def userupload():
    return render_template("userupload.html")

@app.route("/userviewprofile")
def userviewprofile():
    return render_template("userviewprofile.html")


if __name__=="__main__":
    app.run(debug=True)