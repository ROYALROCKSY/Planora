# planora_app/utils.py
from datetime import datetime, timezone
from bson import ObjectId
from planora_app.extensions import get_db

def check_and_update_quota(user_id: str, tokens_needed: int) -> bool:
    """
    Check if user has enough daily quota left.
    If yes, subtract tokens and return True.
    Otherwise return False.
    
    Handles daily reset using UTC dates.
    """
    db = get_db()

    # Make sure user_id is an ObjectId
    if not isinstance(user_id, ObjectId):
        user_id = ObjectId(user_id)

    user = db.users.find_one({"_id": user_id})
    if not user:
        return False  # User not found

    # Reset quota if it's a new day
    last_reset = user.get("quota_last_reset")
    now_utc = datetime.now(timezone.utc)

    if not last_reset or now_utc.date() > last_reset.date():
        db.users.update_one(
            {"_id": user_id},
            {"$set": {"tokens_used": 0, "quota_last_reset": now_utc}}
        )
        user["tokens_used"] = 0

    # Check if enough quota remains
    if user.get("tokens_used", 0) + tokens_needed > user.get("daily_quota", 0):
        return False  # Not enough quota

    # Subtract tokens_used
    db.users.update_one(
        {"_id": user_id},
        {"$inc": {"tokens_used": tokens_needed}}
    )

    return True
