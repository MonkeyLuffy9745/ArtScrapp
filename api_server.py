#!.venv/bin/python3
from flask import Flask
from flask_restful import Api
from model.repositories.repository import Repository
from controller.api.article_controller import ArticleController
from controller.api.website_controller import WebsiteController
from Library.api_encoders import APIEncoder

app = Flask(__name__)
api = Api(app)

app.json_encoder = APIEncoder


api.add_resource(WebsiteController, '/website',
                 '/website/<int:id>')
api.add_resource(ArticleController, '/article',
                 '/article/<int:id>')

if __name__ == '__main__':
    Repository.connect()
    app.run(debug=True, port="8000")