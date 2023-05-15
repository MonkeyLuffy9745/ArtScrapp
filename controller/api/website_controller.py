from flask import jsonify, abort
from flask_restful import Resource, reqparse
from model.repositories.website_repositoy import WebsiteRepository
from model.models import Website

class WebsiteController(Resource):
    def get(self, id=None):
        websiteList = WebsiteRepository.get_all()
        if id:
            website = next(
                (website_tmp for website_tmp in websiteList if website_tmp.id == id), None)
            if website:
                return jsonify(website)
            else:
                abort(404, description="Website not found")
        else:
            return jsonify(websiteList)
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('libelle', type=str, required=True,
                            help='libelle is required')
        parser.add_argument('link', type=str, required=True,
                            help='link is required')
        args = parser.parse_args()

        new_website = Website(libelle=args["libelle"], link=args["link"])
        WebsiteRepository.store(new_website)
        return jsonify(new_website)
    
    def patch(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('libelle', type=str, required=False)
        parser.add_argument('link', type=str, required=False)
        args = parser.parse_args()
        
        website = next(
            (w for w in WebsiteRepository.get_all() if w.id == id), None)
        if not website:
            abort(404, description="Website not found")
            
        if args["libelle"]:
            website["libelle"] = args["libelle"]
        if args["link"]:
            website["link"] = args["link"]
        return jsonify(website)
    
    def delete(self, id):
        website = next(
            (website_tmp for website_tmp in WebsiteRepository.get_all() if website_tmp.id == id), None)
        if not website:
            abort(404, description="Website not found")
        WebsiteRepository.delete(website)
        return jsonify({"message": "Website deleted successfully"})