from datetime import datetime
from planora_app.extensions import get_db

def save_note(user_id: str, text: str):
    """
    Insert a new note. Returns the inserted_id.
    """
    db = get_db()
    notes = db.notes
    doc = {
        "user_id": user_id,
        "text": text,
        "created_at": datetime.utcnow()
    }
    result = notes.insert_one(doc)
    return result.inserted_id

def get_latest_note(user_id: str):
    """
    Return the latest note document for this user (or None).
    """
    db = get_db()
    notes = db.notes
    # find_one supports a sort parameter
    doc = notes.find_one({"user_id": user_id}, sort=[("created_at", -1)])
    return doc
