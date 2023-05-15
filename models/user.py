#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherit from the BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
