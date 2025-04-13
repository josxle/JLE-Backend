from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ap_pat = db.Column(db.String(50), nullable=False)
    ap_mat = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Setter: al asignar una contraseña, la encripta automáticamente
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verifica si una contraseña coincide con la almacenada
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
