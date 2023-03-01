from app import app
from controllers.usuarios_controller import UsuariosController
from flask_jwt_extended import jwt_required
from flask import request

# Creamos la ruta para registrar al usuario
@app.route ("/auth/registrar", methods = ['POST'])
def usuariosRegistrar():
    controller = UsuariosController()
    return controller.crearUsuario(request.json) # request.json = data (headers, body, etc)

@app.route("/auth/autenticar", methods=['POST'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.iniciarSesion(request.json)

#Vamos a ptoteger esta ruta con jwt_required(). Para acceder en postman AUTHORIZATION - BEARER TOKEN - TOKEN 
@app.route("/usuarios/listar", methods=['GET'])
@jwt_required()
def usuariosListar():
    controller = UsuariosController()
    return controller.listarUsuarios()

@app.route("/usuarios/buscar/<int:usuario_id>", methods=['GET'])
def usuariosBuscar(usuario_id):
    controller = UsuariosController()
    return controller.buscarUsuarios(usuario_id)