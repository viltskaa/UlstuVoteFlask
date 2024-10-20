from flask import Flask

from database import close_db
from handlers import teacher_blueprint

app = Flask(__name__)

app.register_blueprint(teacher_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.teardown_appcontext(lambda _: close_db())
    app.run()
