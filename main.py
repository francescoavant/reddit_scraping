from flask import Flask
from flask_restx import Api
from scraping import api as reddit_scraping
from connection import *

app = Flask(__name__)

api = Api(app)
api.add_namespace(reddit_scraping)


if __name__ == "__main__":
        app.run( port=5000, debug=True)
       