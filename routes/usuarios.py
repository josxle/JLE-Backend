from flask import Blueprint, request, jsonify
from models.usuarios import Usuario
from db import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': u.id,
        'nombre': u.nombre,
        'ap_pat': u.ap_pat,
        'ap_mat': u.ap_mat,
        'email': u.email
    } for u in usuarios])

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo = Usuario(
        nombre=data['nombre'],
        ap_pat=data['ap_pat'],
        ap_mat=data['ap_mat'],
        email=data['email'],
        password_hash=data['password']  # en producción deberías hashear
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado correctamente'}), 201

@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and usuario.password_hash == password:
        return jsonify({'mensaje': 'Login exitoso', 'usuario_id': usuario.id}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401
