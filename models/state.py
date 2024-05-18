from models.base_model import BaseModel

class State(BaseModel):
    """state class"""
    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)
        self.name = ""
