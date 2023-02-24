from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from app import db

class ServiciosModel(db.Model):
    __tablename__ = 'servicios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    servicio = Column(String(45), nullable=False)
    createdAt = Column(Text, nullable = True)
    doneAt = Column(Text, nullable = True)
    deletedAt = Column(Text, nullable = True)
    precio = Column(Float, nullable=False)
    horario = Column(Text, nullable=False)
    estado = Column(Boolean, default=True)
   

    usuarios_servicios = relationship('UsuariosServiciosModel')

    def __init__(self, servicio, createdAt,doneAt,deleteAt,precio,horario,estado):
        self.servicio = servicio
        self.createdAt=createdAt
        self.doneAt=doneAt
        self.deletedAt=deleteAt
        self.precio = precio
        self.horario = horario
        self.estado = estado

    def convertirJson(self):
        usuarios = []
        for usuario_servicio in self.usuarios_servicios:
            usuarios.append(usuario_servicio.usuario.convertirJson())

        return {
            'id': self.id,
            'servicio': self.servicio,
            'createdAt': self.createdAt,
            'precio': self.precio,
            'horario': self.horario,
            'estado':self.estado,
            'usuarios': usuarios
        }