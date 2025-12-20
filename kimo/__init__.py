from flask import Flask


def create_app():
    app = Flask(__name__)
    from  .views import account
    from .views import blog
    app.register_blueprint(account.ac)
    app.register_blueprint(blog.bg)
    return app