from flask import jsonify
from APP.App import create_app
from flask_script import Manager
from APP.config import Config

app = create_app(Config)

manager = Manager(app=app)


@app.route('/')
def hello_world():
    return jsonify({'hello': 200})


if __name__ == '__main__':
    manager.run()
