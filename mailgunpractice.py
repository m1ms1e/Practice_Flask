import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6e63b31df83c4ef9be4afc85d1d8737f.mailgun.org/messages",
        auth=("api", "key-13154350349d66ca58dc6f9e7065c392"),
        data={"from": "Excited User <mailgun@sandbox6e63b31df83c4ef9be4afc85d1d8737f.mailgun.org>",
              "to": ["mimi.keshani@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})