# Import the Flask library
from flask import Flask
from flask_restful import Resource, Api, reqparse

# Creates app instance
app = Flask(__name__)
api = Api(app)

sources = ['NPR', 'NYT', 'BBC']


class sourcesList(Resource):
    def get(self):
        return sources


api.add_resource(sourcesList, '/sources/')


@app.route("/")
def home():
    return "Hello! Main page for <h1>website</h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run()
