from flask import Flask
from planora_app.extensions import get_db

app = Flask(__name__)
app.secret_key = "dummy_key_for_testing"

@app.route("/")
def home():
    db = get_db()
    users_count = db.users.count_documents({})
    return f"Users in DB: {users_count}"

if __name__ == "__main__":
    app.run(debug=True)
