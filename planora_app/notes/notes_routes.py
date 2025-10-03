from flask import Blueprint, request, jsonify, session
from planora_app.notes.notes_services import save_note, get_latest_note

notes_bp = Blueprint("notes_bp", __name__)

# fallback user id for dev as you requested
FALLBACK_USER_ID = "68dc37187ffd67372e424594"

@notes_bp.route("/notes/save", methods=["POST"])
def save_note_route():
    user_id = session.get("user_id") or FALLBACK_USER_ID
    payload = request.get_json() or {}
    text = (payload.get("text") or "").strip()
    if not text:
        return jsonify({"error": "Note text is required."}), 400

    inserted_id = save_note(user_id, text)
    return jsonify({"success": True, "note_id": str(inserted_id)}), 201

@notes_bp.route("/notes/latest", methods=["GET"])
def latest_note_route():
    user_id = session.get("user_id") or FALLBACK_USER_ID
    note = get_latest_note(user_id)
    if not note:
        return jsonify({"latest_note": None}), 200

    created_at = note.get("created_at")
    created_str = created_at.strftime("%Y-%m-%d %H:%M") if created_at else ""
    return jsonify({
        "latest_note": {
            "_id": str(note.get("_id")),
            "text": note.get("text"),
            "created_at": created_str
        }
    }), 200
