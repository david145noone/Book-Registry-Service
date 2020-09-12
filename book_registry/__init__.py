import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("books.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Presents the documenation"""

    # Open the readme file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class BookList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        books = []

        for key in keys:
            books.append(shelf[key])

        return {'message': 'Success', 'data': books}, 200



api.add_resource(BookList, '/books')