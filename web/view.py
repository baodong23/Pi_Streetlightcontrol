from datetime import datetime
from flask import render_template, request
from web import app
from functools import wraps


@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'homepage.html',
        title='Homepage',
        year=datetime.now().year,
    )
@app.route('/control')
def control():
    return render_template(
        'control.html',
        title='Control',
        year=datetime.now().year,
    )
@app.route('/system')
def system():
    return render_template(
        'system.html',
        title='system',
        year = datetime.now().year,
    )
@app.route('/chart')
def chart():
    return render_template(
        'chart.html',
        title='Chart',
        year = datetime.now().year,
    )
@app.route('/branch1chart')
def chart1():
    return render_template(
        'branch1chart.html',
        title='Chart1',
        year = datetime.now().year,
    )
@app.route('/branch2chart')
def chart2():
    return render_template(
        'branch2chart.html',
        title='Chart2',
        year = datetime.now().year,
    )
@app.route('/branch3chart')
def chart3():
    return render_template(
        'branch3chart.html',
        title='Chart3',
        year = datetime.now().year,
    )
@app.route('/branch4chart')
def chart4():
    return render_template(
        'branch4chart.html',
        title='Chart4',
        year = datetime.now().year,
    )
@app.route('/settinghome')
def settinghome():
    return render_template(
        'settinghome.html',
        title='Settinghome',
        year=datetime.now().year,
    )
@app.route('/setting-branch1')
def setting_branch1():
    return render_template(
        'setting-branch1.html',
        title='Setting-branch1',
        year=datetime.now().year,
    )
@app.route('/setting-branch2')
def setting_branch2():
    return render_template(
        'setting-branch2.html',
        title='Setting-branch1',
        year=datetime.now().year,
    )
@app.route('/setting-branch3')
def setting_branch3():
    return render_template(
        'setting-branch3.html',
        title='Setting-branch1',
        year=datetime.now().year,
    )
@app.route('/setting-branch4')
def setting_branch4():
    return render_template(
        'setting-branch4.html',
        title='Setting-branch1',
        year=datetime.now().year,
    )