from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuración de la Base de Datos SQLite
db_path = os.path.join(os.path.dirname(__file__), 'usuarios.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la Base de Datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_apellido = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False) # Registro a elección
    password_hash = db.Column(db.String(200), nullable=False)

# Crear la base de datos al iniciar
with app.app_context():
    db.create_all()

@app.route('/registro', methods=['POST'])
def registrar():
    data = request.get_json()
    
    # Hasheo de la contraseña
    hashed_pw = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    nuevo_usuario = Usuario(
        nombre_apellido=data['nombre_apellido'],
        correo_electronico=data['correo'],
        password_hash=hashed_pw
    )
    
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(nombre_apellido=data['nombre_apellido']).first()
    
    if usuario and check_password_hash(usuario.password_hash, data['password']):
        return jsonify({"message": f"Bienvenido {usuario.nombre_apellido}, validación correcta."}), 200
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401

@app.route('/')
def index():
    return "<h1>Examen Final CCNA DEVNET - Sistema de Usuarios</h1><p>Servidor Flask funcionando correctamente.</p>"

if __name__ == '__main__':
    # Configuración del Puerto 7890
    print("Servidor corriendo en el puerto 7890...")
    # El host='0.0.0.0' es fundamental para Docker
    app.run(host='0.0.0.0', port=7890, debug=True)