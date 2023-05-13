from flask import*

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/loginl',methods =['POST',"GET"])
def loginl():
        NAME =request.form['NAME']
        EMAIL = Request.form['EMAIL']
        if NAME == "Tamilselvam" and  EMAIL =="tamil2002selvam@gmail.com":
            return "Welcome to portal"
        else:
            return render_template("register.html")

@app.route('/register1', methods = ['POST','GET'])
def register1():
    NAME =request.form['NAME']
    EMAIL =request.form['EMAIL']
    PASSWORD =request.form['PASSWORD']
    return render_template("login.html")

if __name__  =="_main_" :
    app.run(debug=True,port =5000,host='0.0.0.0')
   
