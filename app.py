from flask import Flask, render_template,request,session
import random
from flask_session import Session
#from DateTime import DateTime
import datetime
app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


#   Pagina Inicial donde podemos dirigirnos a las demas

@app.route('/')
def init():
    return render_template('init.html')

#       FORMS

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/hello',methods=["POST"])
def hello():

    #now = datetime.datetime.now()
    #new_year=now.month==1 and now.date==1
    name_=  request.form.get("name")
    return render_template("hello.html",name=name_)

#   Sin categoria


@app.route('/about')
def about():
    return "About Page."


#       INHERITANCE

@app.route('/page_01_i')
def page_01_inh():
    return render_template("page_01_inh.html")


@app.route('/page_02_i')
def page_02_inh():
    return render_template("page_02_inh.html")


#Looops


@app.route('/loop_page')
def def_loop_field():
    name_list_=[
        "n_f_01",
        "n_f_02",
        "n_f_03",
        "n_f_04",
        "n_f_05",
        "n_f_06",
        "n_f_0 siete",
        "n_f_0 ocho",
        "n_f_0 nueve",
        "n_f_0 diez",
        "n_f_0 once",
        "n_f_0 once",
        ]
    return render_template("loop.html",names_list=name_list_)



#       CONDITIONS

@app.route('/datetime_exerc')
def route_datetime():
    now_data=datetime.datetime.now()
    new_year_=now_data.month==1 and now_data.day==1
    return render_template("datetime.html",new_year=new_year_,now_field=now_data)


#       MACROS
#           no entiendo

notes=[]

@app.route('/macros_page',methods=["GET","POST"])
def macros_link():
    if request.method=="POST":
        note=request.form.get("note")
        notes.append(note)
    return render_template("index_macros.html",notes=notes)




#       NOTES

notes_02=[]
@app.route("/notes_ex", methods=["GET", "POST"])
def route_notes():
    if request.method=="POST":
        note_field_01=request.form.get("note")
        notes_02.append(note_field_01)

    return render_template("index_notes.html",notes_02_field=notes_02)


#       ROUTES0
#           el enrutamiento se usa en todo

#       ROUTES1


@app.route("/route_01/<string:text_message>")
def route_01_dinamic(text_message):
    mensaje_dinamico=text_message;
    return render_template("routes_01.html",mensage=mensaje_dinamico)
    


#       URLS <-- cuando declaro el url_for en todas
# 
#       TEMPLATES <-- usado en todas los enrutamibne y herenia de la plantilla base
#       VARIABBLES <-- creada dento del decorator




#       VARIABLES0
#           pasa un valor como parametro en el render_template



#       VARIABLES_01

@app.route("/var_01")
def route_var_01():
    headline_=random.choice([
        "Hello, World",
        "Hi. there",
        "Good Morning",
        "message 000",
        "message 002",
        "message 003",
        "message 004",
        "message 005"
        ])
    return render_template("var_01.html",headline_field=headline_)


app.run(
            debug=True,
            passtrough_errors=True,
            use_debugger=False,
            use_reloader=False
        )
