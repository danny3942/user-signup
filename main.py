from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

erv = False
eru = False
erm = False

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register' , methods=['POST' , 'GET'])
def register():
    username = request.form['username']
    password = request.form['password']
    ver = request.form['verify']
    email = request.form['email']
    if ver != password:
        erv = True
        return render_template('login.html' , errv=erv , err_mssg="Password does not match!")

    elif password is None or password == "":
        erv = True
        return render_template('login.html' , errv=erv , err_mssg="Must have a password!")

    elif password == username:
        erv = True
        return render_template('login.html' , errv=erv , err_mssg="Password cannot be the same as username!")

    elif len(username) < 3 or len(username) > 20:
        eru = True
        return render_template('login.html' , erru=eru , erru_mssg="Username must be between 3 and 20 characters")

    for char in username:
        if char=='!' or char=="?" or char=="@" or char=="#" or char=="$" or char=="%" or char=="^":
            eru = True
            return render_template('login.html' , erru=eru , erru_mssg="Username cannot contain symbols")

        elif char=="&" or char=="*" or char=="(" or char==")" or char=="+" or char=="=":
            eru = True
            return render_template('login.html' , erru=eru , erru_mssg="Username cannot contain symbols")

    if not(email is None or email == ''):
        counta = 0
        countdot = 0
        for char in email:
            if char == '@':
                counta+=1
                if counta > 1:
                    erm = True
                    return render_template('login.html' , errm=erm , errm_mssg="Email cannot contain more than one @")

            if char == '.':
                countdot+=1
                if countdot > 1:
                    erm = True
                    return render_template('login.html' , errm=erm , errm_mssg="Email cannot contain more than one .")
        if counta < 1 or countdot < 1:
            erm = True
            return render_template('login.html' , errm=erm , errm_mssg="Email must have one @ and one .")

    return render_template('register.html' , name=username)

if __name__ == '__main__':
    app.run()