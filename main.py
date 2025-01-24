from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from datetime import datetime

class Quest(BaseModel):
    title: str
    is_completed: bool = False
    description: str = None
    deadline: datetime

quests = [
    {
        "id": 1,
        "title": "Slay the Dragon",
        "is_completed": False,
        "description": "Defeat the dragon terrorizing the village.",
        "deadline": "2024-01-31"
    },
    {
        "id": 2,
        "title": "Find the Lost Treasure",
        "is_completed": False,
        "description": "Locate the ancient treasure hidden in the Forbidden Forest.",
        "deadline": "2024-02-10"
    },
    {
        "id": 3,
        "title": "Save the Princess",
        "is_completed": False,
        "description": "Rescue the princess trapped in the tower guarded by ogres.",
        "deadline": "2024-02-20"
    },
    {
        "id": 4,
        "title": "Build a Castle",
        "is_completed": False,
        "description": "Construct a fortress to protect your kingdom.",
        "deadline": "2024-03-01"
    },
]
completed_quests = []
current_id = max(quest["id"] for quest in quests) if quests else 0

app = FastAPI()

@app.post("/quests/", tags=["Quests"], summary="Create a new quest", description="Add a new quest to the tracker.")
def create_quest(
    title: str = Form(..., description="The title of the quest"),
    is_completed: bool = Form(False, description="Whether the quest is completed"),
    description: str = Form(None, description="Details about the quest"),
    deadline: str = Form(..., description="Deadline for the quest in YYYY-MM-DD format")
):
    global current_id
    current_id += 1
    new_quest = {
        "id": current_id,
        "title": title,
        "is_completed": is_completed,
        "description": description,
        "deadline": deadline,
    }
    quests.append(new_quest)
    return new_quest

@app.get("/quests", tags=["Quests"], summary="Retrieve all quests", description="Get a list of all quests.")
def get_quests():
    return quests

@app.get("/quests/{quest_id}", tags=["Quests"], summary="Get a quest by ID", description="Retrieve a specific quest by its ID.")
def get_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            return quest
    raise HTTPException(status_code=404, detail="Quest not found")

@app.get("/completed_quests", tags=["Quests"], summary="Get completed quests", description="Retrieve all completed quests.")
def get_completed_quests():
    return completed_quests

@app.put("/quests/{quest_id}", tags=["Quests"], summary="Complete a quest", description="Mark a specific quest as completed.")
def complete_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            quest["is_completed"] = True
            completed_quests.append(quest)
            quests.remove(quest)
            return {"message": f"Quest '{quest['title']}' is marked as completed!"}
    raise HTTPException(status_code=404, detail="Quest not found")

@app.delete("/quests/{quest_id}", tags=["Quests"], summary="Abandon a quest", description="Remove a quest from the tracker.")
def abandon_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            quests.remove(quest)
            return {"message": f"Quest '{quest['title']}' abandoned."}
    raise HTTPException(status_code=404, detail="Quest not found")
