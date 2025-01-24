from fastapi import APIRouter, HTTPException, Form
from ..models import Quest
from ..services.quest_service import create_quest, get_quests, get_quest, get_completed_quests, complete_quest, abandon_quest

router = APIRouter()

@router.post("/", tags=["Quests"], summary="Create a new quest", description="Add a new quest to the tracker.")
def create_quest_route(
    title: str = Form(..., description="The title of the quest"),
    is_completed: bool = Form(False, description="Whether the quest is completed"),
    description: str = Form(None, description="Details about the quest"),
    deadline: str = Form(..., description="Deadline for the quest in YYYY-MM-DD format")):
    return create_quest(title, is_completed, description, deadline)

@router.get("/", tags=["Quests"], summary="Retrieve all quests", description="Get a list of all quests.")
def get_quests_route():
    return get_quests()

@router.get("/completed", tags=["Quests"], summary="Get completed quests", description="Retrieve all completed quests.")
def get_completed_quests_route():
    return get_completed_quests()

@router.get("/{quest_id}", tags=["Quests"], summary="Get a quest by ID", description="Retrieve a specific quest by its ID.")
def get_quest_route(quest_id: int):
    return get_quest(quest_id)

@router.put("/{quest_id}", tags=["Quests"], summary="Complete a quest", description="Mark a specific quest as completed.")
def complete_quest_route(quest_id: int):
    return complete_quest(quest_id)

@router.delete("/{quest_id}", tags=["Quests"], summary="Abandon a quest", description="Remove a quest from the tracker.")
def abandon_quest_route(quest_id: int):
    return abandon_quest(quest_id)
