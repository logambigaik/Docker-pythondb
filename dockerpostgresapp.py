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
    db.execute("CREATE TABLE IF NOT EXISTS Userdetail(number BIGINT,firstname VARCHAR(20),lastname VARCHAR(20),timestamp BIGINT)")	
    db.commit()
 			
    if request.method == "POST":
        details = request.form
        add_new_row(n)
        firstName = details['fname']
        lastName = details['lname']
        #cur1=db.cursor()
        db.execute("INSERT INTO Userdetail(number,firstname, lastname,timestamp) VALUES (:number,:fname, :lname,:timestamp)",{str(n),"fname":firstName,"lname":lastName,str(int(round(time.time() * 1000)))})
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
    app.run(debug=True)
    
     while True:
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(5)
    
