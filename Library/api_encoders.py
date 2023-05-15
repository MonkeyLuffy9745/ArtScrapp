import json
from ..model.models import Website, Article

class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Website):
            return obj.__json__()
        elif isinstance(obj, Article):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)