from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.testing import db
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


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "The task could not be added"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks, title=index)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        "The task could ot be deleted"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')

        except:
            "Task cannot be updated at the moment, Please try adding another task."

    else:
        return render_template('update.html', task=task, title=update)


if __name__ == '__main__':
    app.run(debug=True)
    # app.debug(value=True)
