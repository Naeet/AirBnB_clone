from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class"""
    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
        self.name = ""