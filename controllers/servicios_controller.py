from models.servicios_model import ServiciosModel
from models.usuarios_servicios_model import UsuariosServiciosModel
from app import db

class ServiciosController:

    def crearServicio(self, data):
        try:
            servicio = ServiciosModel(data['servicio'], 
                                      data['createdAt'],
                                      data['doneAt'],
                                      data['deleteAt'],
                                      data['precio'],
                                      data['horario'],
                                      data['estado'])
            db.session.add(servicio)
            db.session.commit()

            nuevos_usuarios = []
            for usuario in data['usuarios']:
                nuevo_usuario = UsuariosServiciosModel(servicio.id, usuario['usuario_id'])
                nuevos_usuarios.append(nuevo_usuario)
            db.session.add_all(nuevos_usuarios)
            db.session.commit()
            return {
                'data': servicio.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarServicios(self):
        servicios = ServiciosModel.query.all()
        response = []
        for servicio in servicios:
            response.append(servicio.convertirJson())
        return {
            'data': response
        }, 200

    def eliminarServicio(self, servicio_id):
        try:
            servicio = ServiciosModel.query.filter_by(id=servicio_id).first()
            servicio.estado = False
            db.session.commit()
            return {
                'message': 'Servicio eliminado correctamente'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarServicio(self, servicio_id, data):
        try:
            servicio = ServiciosModel.query.filter_by(id=servicio_id).first()
            servicio.servicio = data['servicio']
            servicio.precio = data['precio']
            servicio.horario = data['horario']
            db.session.commit()
            return {
                'data': servicio.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
