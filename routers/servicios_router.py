from app import app
from controllers.servicios_controller import ServiciosController
from flask import request
from flask_jwt_extended import jwt_required


@app.route("/servicios/crear", methods=['POST'])
def serviciosCrear(): #definimos la funcion
    controller = ServiciosController() # nuestro contolador
    return controller.crearServicio(request.json) # lo que se va a retornar

#Vamos a ptoteger esta ruta con jwt_required(). Para acceder en postman AUTHORIZATION - BEARER TOKEN - TOKEN 
@app.route("/servicios/listar", methods=['GET'])
@jwt_required()
def serviciosListar():
    controller = ServiciosController()
    return controller.listarServicios()

@app.route("/servicios/eliminar/<int:servicio_id>", methods=['DELETE'])
def serviciosEliminar(servicio_id): #recibimos en la funcion
    controller = ServiciosController()
    return controller.eliminarServicio(servicio_id) #lo enviamos al metodo


@app.route("/servicios/actualizar/<int:servicio_id>", methods=['PUT'])
def serviciosActualizar(servicio_id):
    controller = ServiciosController()
    return controller.actualizarServicio(servicio_id, request.json)




