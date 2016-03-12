from flask import Flask
from flask import render_template
from flask import request
import requests


app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("mailgunapp_hello.html")

@app.route("/signup", methods=['POST'])


def send_simple_message():
    email = request.form['email']
    name = request.form['name']
    requests.post(
        "https://api.mailgun.net/v3/sandbox6e63b31df83c4ef9be4afc85d1d8737f.mailgun.org/messages",
        auth=("api", "key-13154350349d66ca58dc6f9e7065c392"),
        files=[("attachment", open("files/giphy.gif"))],
        data={"from": "Mimi Mailgun <miriam.keshani@gmail.com>",
              "to": email,
              "subject": "Hello {0}".format(name),
              "text": "Hello {0}. Testing some Mailgun awesomness!".format(name),
              "html": "<html><h1>BIG HEADER</h1></html>",
              "o:deliverytime": "Thu, 3 March 2016 17:00:00 GMT"})
    return "All done!"

app.run(	
	debug=True, port=5000
)