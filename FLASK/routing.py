from flask import Flask,render_template,request,abort,session
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import text
from encryption import encode as e,decode as d
from flask_mail import Mail, Message
    
app = Flask(__name__)
app.secret_key = 'a8f$#1kjsdf8sdfjlkj23lkj4!@#lkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
data= SQLAlchemy(app)
class site(data.Model):
    id = data.Column(data.Integer,primary_key=True)
    name = data.Column(data.String(80), nullable=False)
    email = data.Column(data.String(120), nullable=False,unique=True)
    password = data.Column(data.String(120), nullable=False)
    def __repr__(self):
        return f"site('{self.id}','{self.name}', '{self.email}','{self.password}')"


@app.route('/')
def ppt():
    return render_template("ppt.html")

@app.route('/index')
def index(): 
    return render_template('index.html')

@app.errorhandler(404)
def page(e):
    return render_template("error404.html"),404

@app.route('/signup', methods=["GET","POST"])
def signup():
    data1=site.query.all()
    idi=len(data1)+1
    if request.method=="POST":
        id=idi
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        Cpassword=request.form["Cpassword"]
        if email in [i.email for i in data1]:
            return render_template('error_1800.html')
        else:
            data3=site(id=id,name=name,email=email,password=e(password))
            data.session.add(data3)
            data.session.commit()
            return render_template("login.html")
    return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    data1=site.query.all()
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        if email not in [i.email for i in data1]:
            return abort(404)
        else:
            for i in data1:
                if i.email==email and d(i.password)==password:
                    data=[{
                    'id':i.id,
                    'name':i.name,
                    'email':i.email,
                    'password':d(i.password)
                    }]
                    session['Fdata'] = data
                    return render_template('front.html',dat=session.get('Fdata', None))
            else:
                return render_template('wrongemail.html')
    return render_template("login.html")

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["Cpassword"]
        user = site.query.filter_by(email=email).first()
        if not user or d(user.password) != password:
            return render_template('error_notfound.html')
        data.session.delete(user)
        data.session.commit()
        return render_template('sucssout.html')
    return render_template('signout.html') 

@app.route('/sucssout')
def sucssout():
    return render_template('sucssout.html')

@app.route('/front')
def front():
    return render_template("front.html")

@app.route('/profile')
def profile(): 
    p=session.get('Fdata', None)
    return render_template("profile.html", data=p)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/myprofile')
def myprofile():
    return render_template("profile1.html")

# Configure mail ONCE
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'sastitva722@gmail.com'
app.config['MAIL_PASSWORD'] = 'rdxf xwoj gnmx swev'
mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        gmail = request.form["email"]
        name = request.form["name"]
        query = request.form["query"]

        msg = Message(
            'Contact Form Submission',
            sender=app.config['MAIL_USERNAME'],  # Always your email
            recipients=['sastitva722@gmail.com']  # Your email to receive messages
        )
        msg.body = f"Name: {name}\nEmail: {gmail}\nQuery: {query}"
        mail.send(msg)
        return render_template("front.html")
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True,port=6060)