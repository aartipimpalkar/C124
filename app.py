from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! How are u doing in Python?"

if __name__ == '__main__':
    app.run(debug=True)