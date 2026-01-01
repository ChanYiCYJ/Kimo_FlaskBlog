import markdown
from flask import Blueprint, render_template, request, session, jsonify

from Kimo.config import load_config
from utils import db

bg=Blueprint('archive',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    dsb = session.get('user_role')
    post = db.fetchall('select * from blog')
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html', dashboard=dsb, page_title=config["title"],
                               page_subtitle=config["introduction"], config=config, posts=post)


    return post

@bg.route('/archive/<string:archive_title>',methods=['GET','POST'])
def archive(archive_title):

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

        return render_template('archive.html', page_title=archive_page['title'],
                               page_subtitle=f"Created: {archive_page['created']}", article=archive_page,
                               content=content)

    return archive


@bg.route('/post', methods=['GET', 'POST'])
def archive_post():
    check_user = session.get('user_role')
    if check_user == 0:
        config = load_config('app', 'config')
        if request.method == 'GET':
            return '不支持GET调用'

        if request.method == 'POST':
            print('执行post')
            title = request.json.get('title')
            content = request.json.get('content')
            print(content)
            if not content:
                return jsonify({'message': '内容为空'}), 400

            try:
                db.implement('insert into blog(title,content) values (%s,%s)', [title, content])
            except Exception as e:
                return jsonify({'message': str(e)}), 500

            return jsonify({'message': 'ok'})

    return '无权访问'


@bg.route('/edit', methods=['POST'])
def archive_edit():
    check_user = session.get('user_role')
    if check_user == 0:
        if request.method == 'POST':
            post_id = request.json.get('post_id')
            result = db.fetch_one('select * from blog where id=%s', [post_id, ])
            if result:
                return result
            return jsonify({'message': '没有这篇文章'}), 400
    return '无权访问', 400


@bg.route('/delete', methods=['POST'])
def archive_delete():
    check_user = session.get('user_role')
    if check_user == 0:
        post_id = request.json.get('post_id')
        check = db.fetch_one('select * from blog where id=%s', [post_id, ])
        if check:
            db.implement('delete from blog where id=%s', [post_id, ])
            return jsonify({'message': '删除成功'})

        return jsonify({'message': '没有这篇文章'}), 400
    return '无权访问', 400
