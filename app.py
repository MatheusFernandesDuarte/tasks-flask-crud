from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página Sobre"

# isso só serve para o desenvolvimento local, porque o __name__ não é = "__main__" quando é executado por terceiros.
if __name__ == "__main__":
    app.run(debug=True)