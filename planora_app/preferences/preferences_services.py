from bson import ObjectId

def get_user_preferences(db, user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return {}
    return user.get("qna", {})

def update_user_preferences(db, user_id, form_data):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return

    qna = user.get("qna", {})

    # Handle normal fields
    qna["sleep_schedule"] = form_data.get("sleep_schedule", [""])[0]
    qna["morning_evening_person"] = form_data.get("morning_evening_person", [""])[0]
    qna["motivation"] = form_data.get("motivation", [""])[0]
    qna["age"] = form_data.get("age", [""])[0]
    qna["dob"] = form_data.get("dob", [""])[0]
    qna["preferred_time"] = form_data.get("preferred_time", [""])[0]

    # Handle subjects (list)
    qna["subjects"] = form_data.get("subjects", [])

    # Handle difficulties (list)
    difficulties = form_data.get("difficulties", [])
    custom_difficulty = form_data.get("custom_difficulty", [""])[0]
    if custom_difficulty:
        difficulties.append(custom_difficulty)
    qna["difficulties"] = difficulties

    # Handle custom motivation
    custom_motivation = form_data.get("custom_motivation", [""])[0]
    if custom_motivation:
        qna["motivation"] = custom_motivation

    db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"qna": qna}}
    )
