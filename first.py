from  flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s!'%name

if __name__ == '__main__':
    app.run(debug=True)