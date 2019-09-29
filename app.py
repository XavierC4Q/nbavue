from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    if __name__ == 'app':
        from teams import teams_bp
        app.register_blueprint(teams_bp)
        app.run(debug=True)

    return app



