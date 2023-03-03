from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")
@app.get('/<toDisplay>')
def Display(toDisplay):
    return render_template("display.html", todisplay=toDisplay)

if __name__ == '__main__':
    app.run(debug=True)
