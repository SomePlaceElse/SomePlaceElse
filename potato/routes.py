import logging
import json
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, abort

app = Flask(__name__)
# Keeps Flask from swallowing error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config.from_pyfile('analyzeapp.cfg')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/testjson', methods=['POST'])
def test():
    if request.method == 'POST':
        app.logger.warning('RECIEVED test REQUEST!!!')
        print('printing json %r' % request.json)

    return 'OK'

@app.route('/wifilist')
def listWifi():
    return render_template('wifiIndex.html',
            wifi = Analyze.query.order_by(Analyze.added_date.desc()).all()
            )

@app.route('/scanlist')
def listScan():
    return render_template('scanIndex.html',
            scans = Scans.query.order_by(Scans.added_date.desc()).limit(150).all()
            )

@app.route('/newtodo', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        todo = Todo(request.form['title'], request.form['text'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/todos')
def todos():
    return render_template('index.html',
            todos=Todo.query.order_by(Todo.pub_date.desc()).all()
            )

    if __name__ == "__main__":
        app.run()
