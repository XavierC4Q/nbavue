from flask import Flask
from teams import teams_bp

app = Flask(__name__)

app.register_blueprint(teams_bp)
app.run(debug=True)
