# import sys
# sys.path.append("./")
from flask import Flask
from flask_json import FlaskJSON
from flask_restful import Api
from model.models import Website, Article
from model.repositories.repository import Repository
from controller.api.website_controller import WebsiteController
from controller.api.article_controller import ArticleController
app = Flask(__name__)
json = FlaskJSON(app)

@json.encoder
def encoder(obj):
    if isinstance(obj, Website):
        return obj.__json__()
    elif isinstance(obj, Article):
        return obj.__json__()


api = Api(app)
Repository.connect()
api.add_resource(WebsiteController, "/website", "/website/<int:id>")
api.add_resource(ArticleController, "/article", "/article/<int:id>")
if __name__ == "__main__":
    app.run(debug=True, port="8000")