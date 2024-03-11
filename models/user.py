#!/usr/bin/python3
"""
module for user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    handles user information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
