from planora_app.extensions import get_db
from bson.objectid import ObjectId
from datetime import datetime

db = get_db()

def get_subjects(user_id):
    """Fetch subjects from user's qna."""
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return []
    return user.get("qna", {}).get("subjects", [])

# def save_pomodoro_session(data):
#     """Save Pomodoro session in DB."""
#     start_time_dt = datetime.fromisoformat(data["start_time"])
#     end_time_dt = datetime.fromisoformat(data["end_time"])
#     session_doc = {
#         "user_id": ObjectId(data["user_id"]),
#         "subject": data["subject"],
#         "start_time": start_time_dt,
#         "end_time": end_time_dt,
#         "no_of_cycles_decided": data["no_of_cycles_decided"],
#         "no_of_cycles_completed": data["no_of_cycles_completed"],
#         "break_time": data["break_time"],
#         "pause_count": data["pause_count"],
#         "timer_per_cycle": data["timer_per_cycle"],
#         "completion_status": data["completion_status"],
#         "date": start_time_dt.strftime("%Y-%m-%d"),
#     }
#     result = db.sessions.insert_one(session_doc)
#     return result.inserted_id

def save_pomodoro_session(data):
    """Save Pomodoro session in DB."""
    start_time_dt = datetime.fromisoformat(data["start_time"])
    end_time_dt = datetime.fromisoformat(data["end_time"])
    session_doc = {
        "user_id": ObjectId(data["user_id"]),
        "subject": data["subject"],
        "start_time": start_time_dt,
        "end_time": end_time_dt,
        "no_of_cycles_decided": data["no_of_cycles_decided"],
        "no_of_cycles_completed": data["no_of_cycles_completed"],
        "break_time": data["break_time"],
        "pause_count": data["pause_count"],
        "timer_per_cycle": data["timer_per_cycle"],
        "completion_status": data["completion_status"],
        "date": start_time_dt.strftime("%Y-%m-%d"),
    }
    result = db.sessions.insert_one(session_doc)
    return result.inserted_id
