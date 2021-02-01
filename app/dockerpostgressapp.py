import random
import time
from flask import Flask, render_template,request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta



app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:userpass@hostname:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1@localhost:5432/postgres'
db = SQLAlchemy(app)



@app.route('/',methods=['GET','POST'])

def index():
    #cur=db.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS Userdetail(firstname VARCHAR(20),lastname VARCHAR(20))")	
    db.commit()
 			
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        #cur1=db.cursor()
        db.execute("INSERT INTO Userdetail(firstname, lastname) VALUES (:fname, :lname)",{"fname":firstName,"lname":lastName})
        db.commit()
        db.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
     #app.run(host='0.0.0.0',port=5000,debug=True)
     app.run(debug=True)

