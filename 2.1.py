from  flask import Flask
app = Flask(__name__)

@app.route('/haii/<name>/<lname>')
def hello_name(name,lname):
    return 'hello %s!'%(name + lname)


if __name__ == '__main__':
    app.run(debug=True)