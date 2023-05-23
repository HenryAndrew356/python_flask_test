from flask import Flask, render_template,request
#from DateTime import DateTime
import datetime
app=Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

#decorator
@app.route('/hello',methods=["POST"])
def hello():

    #now = datetime.datetime.now()
    #new_year=now.month==1 and now.date==1
    name_=  request.form.get("name")
    return render_template("hello.html",name=name_)


@app.route('/about')
def about():
    return "About Page."


@app.route('/page_01_i')
def page_01_inh():
    return render_template("page_inh.html")


@app.route('/page_02_i')
def page_02_inh():
    return render_template("page_02_inh.html")

@app.route('/loop_page')
def def_loop_field():
    name_list_=["n_f_01","n_f_02","n_f_03"]
    return render_template("loop.html",names_list=name_list_)

app.run(
            debug=True,
            passtrough_errors=True,
            use_debugger=False,
            use_reloader=False
        )
