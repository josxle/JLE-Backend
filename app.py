from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({" ": "x"})

if __name__ == '__main__':
    app.run(debug=True)