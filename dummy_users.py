# scripts/create_dummy_users.py
from datetime import datetime
from planora_app.extensions import get_db

def create_dummy_users():
    db = get_db()

    users = [
        {
            "username": "alice",
            "email": "alice@example.com",
            "password_hash": "hashed_dummy_pass_1",
            "qna": {
                "age": 20,
                "subjects": ["Math", "Physics", "English"],
                "sleep_schedule": "Night owl",
                "morning_evening_person": "Evening",
                "motivation": "Grades",
                "difficulties": "Procrastination"
            },
            # token/quota fields
            "daily_quota": 5000,            # example quota (tokens)
            "tokens_used": 0,
            "quota_last_reset": datetime.utcnow(),
            "created_at": datetime.utcnow()
        },
        {
            "username": "bob",
            "email": "bob@example.com",
            "password_hash": "hashed_dummy_pass_2",
            "qna": {
                "age": 22,
                "subjects": ["Biology", "Chemistry", "History"],
                "sleep_schedule": "Early bird",
                "morning_evening_person": "Morning",
                "motivation": "Knowledge",
                "difficulties": "Distractions"
            },
            # token/quota fields
            "daily_quota": 5000,
            "tokens_used": 0,
            "quota_last_reset": datetime.utcnow(),
            "created_at": datetime.utcnow()
        }
    ]

    for u in users:
        # Use email as unique key so running script again won't duplicate
        res = db.users.update_one(
            {"email": u["email"]},
            {"$setOnInsert": u},
            upsert=True
        )
        if res.upserted_id:
            print(f"Inserted user {u['username']} with id: {res.upserted_id}")
        else:
            print(f"User {u['username']} already exists (no change).")

if __name__ == "__main__":
    create_dummy_users()
