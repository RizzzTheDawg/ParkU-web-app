from flask import Flask
from application.parking_api import parking_bp
from application.user_api import user_bp

app = Flask(__name__)
app.register_blueprint(parking_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5080)
