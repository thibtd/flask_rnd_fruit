from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_fruit():
    """returns a random fruit"""
    fruits = ["apple", "cherry", "orange"]
    return choices(fruits,k=1)


@app.route("/")
def fruit():
    """return random fruit"""
    my_fruit = random_fruit()
    return render_template("index.html", title="random fruit", fruit=my_fruit)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
