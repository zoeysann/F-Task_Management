from flask import Flask
from flask import render_template, request, redirect, url_for
from datetime import datetime

app=Flask(__name__)

tasks=[
    {"title":'Doing history hw',
     "description": 'i hate history',
     "date": '15-01-2025',
     "status": "DONE"}
        ]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    global tasks

    # title=request.form['title']
    # tasks.append(title)

    if request.method == 'POST':
        task_data = dict(request.form)

        raw_date = task_data.get('date')
        if task_data['date']:
            task_data['date'] = datetime.strptime(raw_date, '%Y-%m-%d').strftime('%d-%m-%Y')

        tasks.append(task_data)
        # tasks.append(request.form)

    return redirect(url_for('home'))

# @app.template_filter('dateformat')
# def dateformat(value):
#     try:
#         return datetime.strptime(value, '%Y-%m-%d').strftime('%d-%m-%Y')
#     except ValueError:
#         return value

app.run(debug=True)
