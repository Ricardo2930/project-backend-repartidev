from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class UsuariosServiciosModel(db.Model):
    __tablename__ = 'usuarios_servicios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    servicio_id = Column(Integer, ForeignKey('servicios.id'))

    usuario = relationship('UsuariosModel')
    servicio = relationship('ServiciosModel')

    def __init__(self, servicio_id, usuario_id) -> None:
        self.servicio_id = servicio_id
        self.usuario_id = usuario_id