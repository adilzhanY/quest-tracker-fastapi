quests = []
completed_quests = []
current_id = 1

def create_quest(quest):
    global current_id
    current_id += 1
    new_quest = {
        "id": current_id,
        "title": quest.title,
        "is_completed": quest.is_completed,
        "description": quest.description,
        "deadline": quest.deadline
    }
    quests.append(new_quest)
    return new_quest

def get_quests(is_completed=None):
    if is_completed is None:
        return quests
    return [quest for quest in quests if quest["is_completed"] == is_completed]

def get_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            return quest
    raise HTTPException(status_code=404, detail="Quest not found")

def complete_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            quest["is_completed"] = True
            completed_quests.append(quest)
            quests.remove(quest)
            return {"message": f"Quest '{quest['title']}' is marked as completed!"}
    raise HTTPException(status_code=404, detail="Quest not found")

def abandon_quest(quest_id: int):
    for quest in quests:
        if quest["id"] == quest_id:
            quests.remove(quest)
            return {"message": f"Quest '{quest['title']}' abandoned."}
    raise HTTPException(status_code=404, detail="Quest not found")
