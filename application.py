from flask import Flask, render_template,request
from flaskext.mysql import MySQL
import pymysql

app= Flask(__name__)

mysql=pymysql.connect(db='flaskapp', user='root', passwd='root', host='localhost')

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur=mysql.cursor()
        cur.execute("INSERT INTO Myuser(firstname, lastname) VALUES (%s, %s)", (firstName, lastName))
        mysql.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=5000,debug=True)
    app.run(debug=True)
