from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/history")
def history():
    return render_template('history.html')


@app.route("/rent")
def rent():
    return render_template('rent.html')


@app.route("/group")
def rent():
    return render_template('group.html')


if __name__ == '__main__':
    app.run(debug=True)
