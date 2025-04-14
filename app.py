from flask import Flask, jsonify
from config import Config
from db import db
from flask_cors import CORS

# Rutas
from routes.usuarios import usuarios_bp

# Modelos
from models.usuarios import Usuario

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

app.register_blueprint(usuarios_bp)

@app.route('/')
def index():
    return jsonify({" ": "x"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)