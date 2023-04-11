from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("aboutme.html")


@app.route('/edu')
def index_edu():
    return render_template("edu.html")


@app.route('/contact')
def index_con():
    return render_template("Contact.html")


@app.route('/tech')
def index_tech():
    return render_template("tech.html")


if __name__ == '__main__':
    app.run()
