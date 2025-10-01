from planora_app.extensions import get_db
from datetime import datetime, timezone

db = get_db()

# Reset tokens_used to 0 and update quota_last_reset to now in UTC
result = db.users.update_many(
    {},
    {
        "$set": {
            "tokens_used": 0,
            "quota_last_reset": datetime.now(timezone.utc)
        }
    }
)

print(f"Modified {result.modified_count} users. Quotas reset.")
