# planora_app/dashboard/cards_routes.py
from flask import Blueprint, request, jsonify ,session
from .cards_services import calculate_best_time
from .cards_services import get_priority_focus
from planora_app.dashboard.cards_services import get_daily_streak

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("/best-time", methods=["GET"])
def get_best_time():
    # For now, get user_id from query params
    user_id = session.get("user_id") or request.args.get("user_id") or "68dc37187ffd67372e424594"
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    result = calculate_best_time(user_id)
    return jsonify(result)


@cards_bp.route("/priority-focus", methods=["GET"])
def priority_focus():
    """
    Returns JSON for priority focus card.
    user_id passed as query param for now: /cards/priority-focus?user_id=...
    """
    user_id = session.get("user_id") or "68dc37187ffd67372e424594"
    if not user_id:
        return jsonify({"error": "user_id query param is required"}), 400

    data = get_priority_focus(user_id)
    return jsonify(data)

@cards_bp.route("/daily-streak", methods=["GET"])
def daily_streak_route():
    # Get user_id from session (auth) or fallback for testing
    user_id = session.get("user_id") or request.args.get("user_id") or "68dc37187ffd67372e424594"

    result = get_daily_streak(user_id)
    return jsonify(result)