from flask import flask

app=Flask(__name__)

@app.route("/")
def home():
    return "hello hey !"

if __name__ == "__main__":
    app.run()    