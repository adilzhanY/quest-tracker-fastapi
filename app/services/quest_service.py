from ..models import Quest
from fastapi import HTTPException
from typing import List
from datetime import datetime, date

quests: List[Quest] = []
completed_quests: List[Quest] = []
current_id = 0

def create_quest(title: str, is_completed: bool, description: str, deadline: str) -> Quest:
    global current_id
    current_id += 1
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()  # Parse the deadline string to a date object
    new_quest = Quest(id=current_id, title=title, is_completed=is_completed, description=description, deadline=deadline_date)
    if new_quest.is_completed == True:
        completed_quests.append(new_quest)
    else:
        quests.append(new_quest)
    return new_quest

def get_quests() -> List[Quest]:
    return quests

def get_completed_quests() -> List[Quest]:
    return completed_quests

def get_quest(quest_id: int) -> Quest:
    for quest in quests:
        if quest.id == quest_id:  # Accessing attributes directly instead of using subscript
            return quest
    raise HTTPException(status_code=404, detail="Quest not found")

def complete_quest(quest_id: int) -> dict:
    for quest in quests:
        if quest.id == quest_id:
            quest.is_completed = True
            completed_quests.append(quest)
            quests.remove(quest)
            return {"message": f"Quest '{quest.title}' is marked as completed!"}
    raise HTTPException(status_code=404, detail="Quest not found")

def abandon_quest(quest_id: int) -> dict:
    for quest in quests:
        if quest.id == quest_id:
            quests.remove(quest)
            return {"message": f"Quest '{quest.title}' abandoned."}
    raise HTTPException(status_code=404, detail="Quest not found")
