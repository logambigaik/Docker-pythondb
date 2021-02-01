import random

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
import os
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:userpass@hostname:5432/testdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1@db:5432/postgres'
db = SQLAlchemy(app)



@app.route('/',methods=['GET','POST'])

def index():
    #cur=db.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS Userdetail(number BIGINT,firstname VARCHAR(20),lastname VARCHAR(20),timestamp BIGINT)")
    db.commit()

    if request.method == "POST":
        details = request.form
        #num=add_new_row(n)
        firstName = details['fname']
        lastName = details['lname']
        #cur1=db.cursor()
        db.execute("INSERT INTO Userdetail(number,firstname, lastname,timestamp) VALUES (" + \
                                           str(num) + ','   + \
                                           firstName + ','  + \
                                           lastName + ','   + \
                                           str(int(round(time.time() * 1000))) + ");")

        db.commit()
        db.close()
        return 'success'
    return render_template('index.html')

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number,firstname,lastname " + \
            "FROM UserDetail " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" +\
            "LIMIT 1"

    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]

if __name__ == '__main__':
     #app.run(host='0.0.0.0',port=5000,debug=True)


     while True:
        num=(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(5)

     app.run(debug=True)

