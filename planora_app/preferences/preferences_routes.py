from flask import Blueprint, render_template, request, redirect, url_for, session
from planora_app.preferences.preferences_services import get_user_preferences, update_user_preferences
from planora_app.extensions import get_db

preferences_bp = Blueprint(
    "preferences",
    __name__,
    template_folder="../templates",  # points to main templates folder
    static_folder="../static",
    url_prefix="/preferences"
)

@preferences_bp.route("/", methods=["GET", "POST"])
def preferences():
    db = get_db()
    user_id = session.get("user_id") or "68dc37187ffd67372e424594"

    if request.method == "POST":
        form_data = request.form.to_dict(flat=False)
        update_user_preferences(db, user_id, form_data)
        return redirect(url_for("preferences.preferences"))

    edit_mode = request.args.get("edit") == "1"
    preferences = get_user_preferences(db, user_id)
    return render_template("preferences.html", preferences=preferences, edit_mode=edit_mode)
