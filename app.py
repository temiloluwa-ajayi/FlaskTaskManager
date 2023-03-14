from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db
from datetime import datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_master.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    # field_name = db.Column(db.variable_type, primary_key, nullable, default, composite_key)
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        pass

    return render_template('index.html', title=index)


if __name__ == '__main__':
    app.run(debug=True)
    # app.debug(value=True)
