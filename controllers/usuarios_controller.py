from models.usuarios_model import UsuariosModel
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_jwt_extended import create_access_token, create_refresh_token

class UsuariosController:
    def __init__(self) -> None: #Metodo mágico
        self.model = UsuariosModel #Definimos nuestro modelo a usar

    def crearUsuario(self, data):
        try:
            password = self.__encriptarContraseña (data ['password']) #La contraseña estará incriptada
            #print(password) -> self.model = UsuariosModel de ahi lo obtiene
            usuario = self.model(data['name'],
                                 password,
                                 data['imagenProfile'], 
                                 data['createdAt'],
                                 data['email'],
                                 data['lastName'],
                                 data['dni'],
                                 data['phone'], 
                                 data['tower'],
                                 data['dpto'],
                                 data['condominio'], 
                                 )
            db.session.add(usuario)
            db.session.commit()
            return {
                'data' : usuario.convertirJson()
                #'data' : 'Contraseña Encriptada'
            }    
        
        except Exception as e:
            return {
                'message' : 'Internal server error',
                'error' :str(e)
            },500

    def iniciarSesion(self, data):
        try:
            # print(data)
            usuario = self.model.query.filter_by(email=data['email']).first() #vamos a buscar al usuario (filtrar) con .first
            #print(usuario)
            if not usuario: #para validar y controlar si el correo y contraseña que existan y sean las correctas
                return {
                    'message' : 'Unauthorized'
                },401
            
            if not check_password_hash(usuario.password, data['password']):
                return {
                    'message' : 'Unauthorized'
                },401 
         
            access_token = create_access_token (identity = {
                'id':usuario.id,
                'email':usuario.email
            }) # aca definimos -- > user_id = get_jwt_identity() en categorias_router, en ruta protegida
            
            refresh_token = create_refresh_token(identity = {
                'id':usuario.id,
                'email':usuario.email
            })
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            } 

        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    
    def listarUsuarios(self):
        usuarios = UsuariosModel.query.all()
        response = []
        for usuario in usuarios:
            response.append(usuario.convertirJson())
        return {
            'data': response
        }, 200
        
    def buscarUsuarios(self, usuarios_id):
        try:
            usuarios_ids = UsuariosModel.query.filter_by(id=usuarios_id)
            #print(usuarios_ids)
            response = []
            for usuario in usuarios_ids:
                response.append(usuario.verServicios())
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def __encriptarContraseña (self, contraseña): #Método privado para encriptar contraseña
        return generate_password_hash (contraseña)