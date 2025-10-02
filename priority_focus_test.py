# priority_focus_test.py
import requests

# Change this to your local server if different
BASE_URL = "http://127.0.0.1:5000"

# Temporary manual user_id
USER_ID = "68dc37187ffd67372e424594"

def test_priority_focus(user_id):
    url = f"{BASE_URL}/cards/priority-focus"
    params = {"user_id": user_id}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        print("Priority Focus Card:")
        print(data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_priority_focus(USER_ID)
