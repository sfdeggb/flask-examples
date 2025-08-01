import click 
from flask import Flask 


app =Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return '<h1> hello,world!</h1>'

@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1> Hello,Flask</h1>'

@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1> Hello,%s!</h1>' %name

@app.cli.command()
def hello():
    click.echo("hello, human!")

