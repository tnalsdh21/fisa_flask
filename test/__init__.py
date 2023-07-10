from flask import Flask


def create_app():
    app = Flask(__name__)

    

    from views import main_views

    app.register_blueprint(main_views.bp)
    return app
#Flask 패키지에 있는 클래스를 통해 
# 어플리케이션의 입구를 만들어준다
