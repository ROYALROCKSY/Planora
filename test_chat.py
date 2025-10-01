# test_chat.py
import requests

# Replace this with a valid user_id from your MongoDB
USER_ID = "68dc37187ffd67372e424594"

# Example message to send
message = "Explain Python in simple words"

# Send POST request to Flask backend
res = requests.post(
    "http://127.0.0.1:5000/chat",
    json={
        "user_id": USER_ID,
        "message": message
    }
)

try:
    print(res.json())
except Exception as e:
    print("Failed to decode JSON response:", e)
    print("Response text:", res.text)
