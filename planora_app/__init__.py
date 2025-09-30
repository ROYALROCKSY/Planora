from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "dummy_key_for_testing"

    # Import and register blueprints
    from planora_app.dashboard.routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app
