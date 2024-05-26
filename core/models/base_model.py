from bson import ObjectId

class BaseModel:
    def __init__(self, data=None):
        if data:
            self._id = data.get('_id', ObjectId())
            self.created_at = data.get('created_at')
            self.updated_at = data.get('updated_at')
            self.status = data.get("status")

    def to_dict(self):
        return self.__dict__
