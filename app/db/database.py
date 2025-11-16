import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.beanie_models import (
    User, Child, Task, Reward, ChildReward, MiniGame,
    GameSession, InteractionLog, Report, ChildTask
)
from app.config import settings

MONGO_URI = settings.DATABASE_URL
DATABASE_NAME = os.getenv("DATABASE_NAME", "kiddy_mate_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

async def init_database():
    await init_beanie(database=db, document_models=[
        User,
        Child,
        Task,
        Reward,
        ChildReward,
        MiniGame,
        GameSession,
        InteractionLog,
        Report,
        ChildTask
    ])