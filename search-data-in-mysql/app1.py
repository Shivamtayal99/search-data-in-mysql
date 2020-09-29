from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('test.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shivam"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        result=request.form
        name=result['Name']

        mycursor.execute("select name,physics,chemistery,maths,total from students where name='"+name+"'")
        r=mycursor.fetchone()
        mydb.commit()
        mycursor.close()
        # return render_template('test.html',result=result)
        return render_template('index.html',r=r)

app.run(debug=True)