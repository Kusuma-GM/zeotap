from flask import Flask # type: ignore

app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return "<h1>Welcome to the Web Sheets App!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
