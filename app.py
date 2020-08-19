from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return (1, 4, 6,)




if __name__ == "__main__":
    app.run(debug=True)