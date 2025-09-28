from planora_app.extensions import get_db
from datetime import datetime

db = get_db()

# Alice
alice_id = db.users.insert_one({
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
    "created_at": datetime.utcnow()
}).inserted_id

# Bob
bob_id = db.users.insert_one({
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
    "created_at": datetime.utcnow()
}).inserted_id

print("Inserted Alice with ID:", alice_id)
print("Inserted Bob with ID:", bob_id)
