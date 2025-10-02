from flask import Blueprint, request, jsonify, render_template
from .timer_services import get_subjects, save_pomodoro_session

timer_bp = Blueprint("timer", __name__, template_folder="templates", url_prefix="/timer")

@timer_bp.route("/")
def timer_home():
    return render_template("timer.html")

@timer_bp.route("/subjects")
def fetch_subjects():
    user_id = request.args.get("user_id")
    subjects = get_subjects(user_id)
    return jsonify({"subjects": subjects})

@timer_bp.route("/save_session", methods=["POST"])
def save_session():
    data = request.get_json()
    session_id = save_pomodoro_session(data)
    return jsonify({"status": "success", "session_id": str(session_id)})
