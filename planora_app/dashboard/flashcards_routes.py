
# planora_app/flashcards/flashcards_routes.py
from flask import Blueprint, request, jsonify
from planora_app.utils import check_and_update_quota
from .flashcards_services import generate_flashcards

flashcards_bp = Blueprint("flashcards", __name__, url_prefix="/flashcards")

# Example token cost per upload (adjust as needed)
TOKENS_PER_UPLOAD = 50

@flashcards_bp.route("/upload", methods=["POST"])
def upload_doc():
    """
    Expects a form-data request with file input: <input type="file" name="file">
    """
    user_id = request.form.get("user_id")
    file = request.files.get("file")  # match frontend

    if not user_id or not file:
        return jsonify({"error": "user_id and file are required"}), 400

    # Check user quota
    from planora_app.utils import check_and_update_quota
    TOKENS_PER_UPLOAD = 50
    if not check_and_update_quota(user_id, TOKENS_PER_UPLOAD):
        return jsonify({"error": "Daily token quota exceeded!"}), 403

    # Read file content
    text = file.read().decode("utf-8")

    # Call service to generate flashcards
    from .flashcards_services import generate_flashcards
    flashcards = generate_flashcards(user_id, text)

    return jsonify({"flashcards": flashcards})

