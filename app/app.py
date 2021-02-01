from flask import Flask, render_template,request
from flask import jsonify
from sqlalchemy import create_engine
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

app=Flask(__name__)
conn_str = 'postgresql://{username}:{password}@localhost:5432/{database}'.format(
            username='postgres',
            password='password1',
            database='postgres'
         )

engine=create_engine(conn_str)
db=scoped_session(sessionmaker(bind=engine))
#db=SQLAlchemy(app)


@app.route('/',methods=['GET','POST'])

def index():
    #cur=db.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS userdetail(firstname VARCHAR(20),lastname VARCHAR(20))")	
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
