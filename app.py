# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        deadline = request.form['deadline']
        task = Task(name, description, deadline)
        tasks.append(task)
        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        deadline = request.form['deadline']
        task = Task(name, description, deadline)
        tasks.append(task)
        return redirect(url_for('index'))

    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)
projectstructure/app.py