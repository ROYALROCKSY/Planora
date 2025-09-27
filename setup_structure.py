import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "planora_app"

list_of_files = [
    # Root level
    "app.py",
    "config.py",
    "requirements.txt",
    ".gitignore",
    "README.md",

    # Instance
    "instance/config.py",

    # Core app
    f"{project_name}/__init__.py",
    f"{project_name}/extensions.py",
    f"{project_name}/models.py",
    f"{project_name}/utils.py",
    f"{project_name}/routes.py",

    # Auth
    f"{project_name}/auth/routes.py",
    f"{project_name}/auth/templates/auth/login.html",
    f"{project_name}/auth/templates/auth/signup.html",

    # Dashboard
    f"{project_name}/dashboard/routes.py",
    f"{project_name}/dashboard/services.py",
    f"{project_name}/dashboard/templates/dashboard/dashboard.html",

    # Preferences
    f"{project_name}/preferences/routes.py",
    f"{project_name}/preferences/templates/preferences/preferences.html",

    # Pomodoro
    f"{project_name}/pomodoro/routes.py",
    f"{project_name}/pomodoro/timer_logic.py",
    f"{project_name}/pomodoro/templates/pomodoro/pomodoro.html",

    # Sessions
    f"{project_name}/sessions/routes.py",
    f"{project_name}/sessions/templates/sessions/session_history.html",

    # Tasks
    f"{project_name}/tasks/routes.py",
    f"{project_name}/tasks/task_logic.py",
    f"{project_name}/tasks/templates/tasks/tasks.html",

    # Notes
    f"{project_name}/notes/routes.py",
    f"{project_name}/notes/templates/notes/notes.html",

    # Insights
    f"{project_name}/insights/routes.py",
    f"{project_name}/insights/charts.py",
    f"{project_name}/insights/templates/insights/insights.html",

    # Challenges
    f"{project_name}/challenges/routes.py",
    f"{project_name}/challenges/logic.py",
    f"{project_name}/challenges/templates/challenges/challenges.html",

    # Summariser
    f"{project_name}/summariser/routes.py",
    f"{project_name}/summariser/summariser_logic.py",
    f"{project_name}/summariser/templates/summariser/summariser.html",

    # Chatbot
    f"{project_name}/chatbot/routes.py",
    f"{project_name}/chatbot/chatbot_service.py",
    f"{project_name}/chatbot/templates/chatbot/chatbot.html",

    # Static
    f"{project_name}/static/css/style.css",
    f"{project_name}/static/js/main.js",
    f"{project_name}/static/images/logo.png",
    f"{project_name}/static/images/achievements/.gitkeep",
    f"{project_name}/static/uploads/docs/.gitkeep",

    # Global templates
    f"{project_name}/templates/layout.html",
    f"{project_name}/templates/index.html",
    f"{project_name}/templates/error.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
