from planora_app.extensions import get_db
from datetime import datetime, timedelta
from bson import ObjectId

def get_user_sessions(user_id: str, filter_type=None, filter_value=None):
    db = get_db()
    query = {"user_id": user_id}

    today = datetime.utcnow().date()

    if filter_type and filter_value:
        if filter_type == "date":
            try:
                dt = datetime.strptime(filter_value, "%Y-%m-%d")
                query["start_time"] = {"$gte": datetime(dt.year, dt.month, dt.day),
                                       "$lt": datetime(dt.year, dt.month, dt.day, 23, 59, 59)}
            except:
                pass
        elif filter_type == "month":
            try:
                month = int(filter_value)
                query["start_time"] = {"$gte": datetime(today.year, month, 1),
                                       "$lt": datetime(today.year, month, 31, 23, 59, 59)}
            except:
                pass
        elif filter_type == "year":
            try:
                year = int(filter_value)
                query["start_time"] = {"$gte": datetime(year, 1, 1),
                                       "$lt": datetime(year, 12, 31, 23, 59, 59)}
            except:
                pass
        elif filter_type == "subject":
            # Case-insensitive subject filter
            query["subject"] = {"$regex": f"^{filter_value}$", "$options": "i"}

    sessions_cursor = db.sessions.find(query).sort("start_time", -1)
    session_list = []

    for sess in sessions_cursor:
        start_time = sess.get("start_time")
        end_time = sess.get("end_time")

        studied_hrs = round((end_time - start_time).total_seconds() / 3600, 2) if start_time and end_time else 0
        decided_cycles = sess.get("no_of_cycles", 0)
        completed_cycles = sess.get("no_of_completed_cycles", 0)

        session_list.append({
            "_id": str(sess["_id"]),
            "subject": sess.get("subject", ""),
            "studied_hrs": studied_hrs,
            "date": start_time.strftime("%Y-%m-%d") if start_time else "",
            "start_time": start_time.strftime("%H:%M") if start_time else "",
            "cycles": f"{completed_cycles}/{decided_cycles}"
        })

    return session_list
