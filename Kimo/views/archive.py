from flask import Blueprint, render_template, request, session
import markdown
from Kimo.config import load_config
from utils import db
bg=Blueprint('archive',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    dsb = session.get('user_role')
    post = db.fetchall('select * from blog')
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html',dashboard=dsb,config=config,posts=post)


    return post

@bg.route('/archive/<string:archive_title>',methods=['GET','POST'])
def archive(archive_title):
    config = {
        "title": "Hello World",
        "content": "Hello World",
    }
    archive_page = db.fetch_one('select * from blog where title=%s', [archive_title, ])
    if request.method=='GET':
        content = markdown.markdown(
    archive_page['content'],
            extensions=[
                "tables",
                "toc",
                "fenced_code",
                "pymdownx.superfences",
                "pymdownx.tasklist",
                "pymdownx.details",
                "pymdownx.inlinehilite",
            ]
)

        print(archive_page)
        return render_template('archive.html',config=config,article=archive_page,content=content)

    return archive

@bg.route('/Dashboard',methods=['POST','GET'])
def archive_post(archive_title):
    return render_template('archive.html')