
from fastapi import APIRouter, HTTPException
from ..models import Quest
from ..services.quest_service import create_quest, get_quests, get_quest, complete_quest, abandon_quest

router = APIRouter()

@router.post("/", tags=["Quests"], summary="Create a new quest", description="Add a new quest to the tracker.")
def create_quest_route(quest: Quest):
    return create_quest(quest)

@router.get("/", tags=["Quests"], summary="Retrieve all quests", description="Get a list of all quests.")
def get_quests_route():
    return get_quests()

@router.get("/{quest_id}", tags=["Quests"], summary="Get a quest by ID", description="Retrieve a specific quest by its ID.")
def get_quest_route(quest_id: int):
    return get_quest(quest_id)

@router.get("/completed", tags=["Quests"], summary="Get completed quests", description="Retrieve all completed quests.")
def get_completed_quests_route():
    return get_quests(is_completed=True)

@router.put("/{quest_id}", tags=["Quests"], summary="Complete a quest", description="Mark a specific quest as completed.")
def complete_quest_route(quest_id: int):
    return complete_quest(quest_id)

@router.delete("/{quest_id}", tags=["Quests"], summary="Abandon a quest", description="Remove a quest from the tracker.")
def abandon_quest_route(quest_id: int):
    return abandon_quest(quest_id)
