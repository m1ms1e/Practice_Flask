from flask import Flask
from flask import render_template
from flask import request

#flask will look in templates folder for files to render
#flask contains requests which we need to get form data

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("practiceflaskhello.html")

#this is a url matcher and takes the paramter from the url - here <name>
@app.route("/<name>")
def hello_someone(name):
	return render_template("practiceflaskhello.html", name=name.title())

@app.route("/bye/<name>")
def bye_someone(name):
	return render_template("practiceflaskbye.html", name=name.title())

#Goodbye without using template:
#@app.route("bye/<name>")
#def goodbye_someone(name):
#	return "Goodbye {0}!".format(name.title())

@app.route("/bye/<name>/night")
def night_someone(name):
	return render_template("practiceflaskbyenight.html", name=name.title())

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form
	print form_data['name']
	print form_data['email']
	return "All OK"
#this prints out the form data in the terminal and returns ALL OK at the url that the template directs to /signup


app.run(	
	debug=True, port=5000
)

#debug=True means everytime you update your file the server will update too. Otherwise will have to restart server every time
#app.run() must always be at the end
#PORT is by default on 5000, if you chanfe the port you have to restart the server in the command line
#ctrl-C stops the server