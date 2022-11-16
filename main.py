import messagebird
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    
    return "hi"

@app.route('/sms', methods=['GET'])
def sms():
    client = messagebird.Client("PPkr7hEy8QPpA9TylB0eZMeLT")
    message = client.message_create(
          'TestMessage',
          '+56940008559',
          'This is a test message',
          { 'reference' : 'Foobar' }
      )
    return "done"

app.run()