from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello from Joseph ECS Container and to see if revision works!'

app.run(host='0.0.0.0', port=8080)
