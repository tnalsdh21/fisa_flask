from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#db에 대한 실제 내용이 작성되어있는 config(db+원격저장소+ 암호화된 ...)
import config 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app,db)
    from views import main_views

    app.register_blueprint(main_views.bp)
    return app
#Flask 패키지에 있는 클래스를 통해 
# 어플리케이션의 입구를 만들어준다
