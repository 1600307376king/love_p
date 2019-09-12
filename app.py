from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import local_setting

app = Flask(__name__)
app.secret_key = local_setting.SECRET_KEY
app.config.from_object('local_setting')

db = SQLAlchemy(app)

from view.match import route_index

app.register_blueprint(route_index, url_prefix="/")

if __name__ == '__main__':
    app.run()

