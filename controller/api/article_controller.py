from flask import jsonify, abort
from flask_restful import Resource
from model.repositories.article_repository import ArticleRepository

class ArticleController(Resource):
    def get(self, id=None):
        articleList = ArticleRepository.get_all()
        if id:
            article = next(
                (article_tmp for article_tmp in articleList if article_tmp.id == id), None)
            if article:
                return jsonify(article)
            else:
                abort(404, description="Article not found")
        else:
            return jsonify(articleList)
        
    def delete(self, id):
        article = next(
            (article_tmp for article_tmp in ArticleRepository.get_all() if article_tmp.id == id), None)
        if not article:
            abort(404, description="Article not found")
        ArticleRepository.delete(article)
        return jsonify({"message": "Article deleted successfully"})