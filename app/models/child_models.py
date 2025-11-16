from beanie import Document, Link
from datetime import datetime
from typing import Optional
from app.models.user_models import User

class Child(Document):
    parent: Link[User]
    name: str
    birth_date: datetime
    initial_traits: Optional[dict]
    current_coins: int = 0
    level: int = 1

    class Settings:
        name = "children"