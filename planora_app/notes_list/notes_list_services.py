from planora_app.extensions import get_db
from datetime import datetime, timedelta
from bson import ObjectId

def get_user_notes(user_id: str, filter_type=None, filter_value=None):
    db = get_db()
    query = {"user_id": user_id}

    today = datetime.utcnow().date()

    if filter_type and filter_value:
        if filter_type == "date":
            try:
                dt = datetime.strptime(filter_value, "%Y-%m-%d")
                query["created_at"] = {"$gte": datetime(dt.year, dt.month, dt.day),
                                       "$lt": datetime(dt.year, dt.month, dt.day, 23, 59, 59)}
            except:
                pass
        elif filter_type == "month":
            try:
                month = int(filter_value)
                query["created_at"] = {"$gte": datetime(today.year, month, 1),
                                       "$lt": datetime(today.year, month, 31, 23, 59, 59)}
            except:
                pass
        elif filter_type == "year":
            try:
                year = int(filter_value)
                query["created_at"] = {"$gte": datetime(year, 1, 1),
                                       "$lt": datetime(year, 12, 31, 23, 59, 59)}
            except:
                pass
        elif filter_type == "starred":
            query["starred"] = True

    notes_cursor = db.notes.find(query).sort("created_at", -1)
    notes_list = []
    for note in notes_cursor:
        text = note.get("text", "")
        # Partial text for display
        snippet = " ".join(text.split()[:35]) + ("..." if len(text.split()) > 35 else "")
        notes_list.append({
            "_id": str(note["_id"]),
            "text": text,
            "snippet": snippet,
            "created_at": note.get("created_at").strftime("%Y-%m-%d %H:%M"),
            "starred": note.get("starred", False)
        })
    return notes_list

def toggle_star_note(note_id, starred: bool):
    db = get_db()
    db.notes.update_one({"_id": ObjectId(note_id)}, {"$set": {"starred": starred}})
