from flask import Flask

app = Flask(__name__)
#new app
@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

