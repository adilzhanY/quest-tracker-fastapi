from fastapi import FastAPI
from app.routes import quests

app = FastAPI()

app.include_router(quests.router, prefix="/quests", tags=["Quests"])
