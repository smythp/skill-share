import sqlite3
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

def make_dict(cursor):
    list_of_dicts = []
    keys_list = []
    for key in cursor.description:
        keys_list.append(key[0])

    for (number,row) in enumerate(cursor.fetchall()):
        dict_out = {}
        for number2,key in enumerate(keys_list):
            dict_out[key] = row[number2]
        list_of_dicts.append(dict_out)

    return list_of_dicts



@app.route('/')
@app.route('/index')
def index():

    conn = sqlite3.connect("skill.db")
    c = conn.cursor()
    out = c.execute("SELECT skill_name,skill_description FROM skill;")

    out = out.fetchall()


    skills = []
    skills_description = []
    for skill in out:
        skills.append(skill[0])
        skills_description.append(skill[1])

    print(skills,skills_description)

    return render_template('index.html',title='Home',skills=skills,skills_description=skills_description)
    
@app.route('/foo')
def foo():
    return 'fuck'

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'],
                           )
