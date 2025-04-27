from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=0.0):
    """calculate and convert celsius given to fahrenheit"""
    celsius = float(celsius)
    fahrenheit = str(celsius * 9.0 / 5 + 32)
    return fahrenheit


if __name__ == '__main__':
    app.run()

