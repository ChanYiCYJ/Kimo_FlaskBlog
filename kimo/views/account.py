from flask import Blueprint, render_template, request
import pymysql
from utils import db
from werkzeug.security import generate_password_hash, check_password_hash
ac=Blueprint('account',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    email=request.form.get('email')
    password=request.form.get('password')
    result=db.fetch_one('select * from userInfo where email=%s and password=%s',[email,password])
    if result:
     return render_template('/index.html')

    return render_template('login.html',error="请重新尝试")

@ac.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    username=request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    result =db.register_user('INSERT INTO userInfo(email,password,user_name) VALUES(%s,%s,%s)',[email,password,username])
    login()

    return render_template('login.html', error="请重新尝试")

@ac.route('/logout')
def logout():
    return "Logout"

@ac.route('/users')
def users():
    return "Users"