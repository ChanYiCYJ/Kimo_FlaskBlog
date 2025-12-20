from flask import Blueprint, render_template, request
from utils import db
bg=Blueprint('blog',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    post = db.fetchall('select * from blog')
    config ={
        "title":"Hello World",
        "content":"Hello World",
    }
    if request.method=='GET':
        return render_template('index.html',config=config,posts=post)

    return post

@bg.route('/archives/<string:post_title>',methods=['GET','POST'])
def post(post_title):
    if request.method=='GET':
        post_page = db.fetch_one('select * from blog where title=%s',[post_title,])
        print(post_page)
        return post_page

    return render_template('post.html',title=post_title,post=post)
