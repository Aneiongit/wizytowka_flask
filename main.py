from flask import Flask
from flask import request, redirect
from flask import render_template
main = Flask(__name__)


@main.route('/about_me', methods=['GET'], endpoint='action1')
def action1():
    return render_template("web1.html")


@main.route('/contact', methods=['GET', 'POST'], endpoint='action2')
def action2():
    if request.method == 'GET':
        return render_template("web2.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/send")


@main.route('/send', methods=['GET'], endpoint='action3')
def action3():
    return render_template("return_message.html")
