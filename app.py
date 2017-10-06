from flask import Flask, render_template, request, session, redirect, url_for
import os

my_app = Flask(__name__)
my_app.secret_key = os.urandom(32)

@my_app.route('/')
def root():
	if session.has_key('name') == True:
		return redirect(url_for('welcome'))
	else:
		return redirect(url_for('login'))

@my_app.route("/response/", methods = ["POST","GET"])
def resp():
	if request.form["username"] == 'user':
		if request.form["password"] != 'pass':
			return render_template("response1.html", text = "Bad password!")
	elif request.form["password"] == 'pass':
		if request.form["username"] != 'user':
			return render_template("response1.html", text = "Bad username!")
	elif request.form["username"] != 'user':
		if request.form["password"] != 'pass':
			return render_template("response1.html", text = "Username and password not recognized")
	session['name'] = "user"
	return render_template("welcome.html", text = session['name'])

@my_app.route('/welcome')
def welcome():
	return render_template('/welcome.html', text = session['name'])

@my_app.route('/login')
def login():
	return render_template('/login.html')

@my_app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('login'))

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()
