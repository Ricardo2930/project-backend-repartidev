from app import db
from sqlalchemy import Column, String, Integer, Text


class UsuariosModel (db.Model):
    __tablename__ = "usuarios"

    id = Column (Integer, primary_key = True, autoincrement = True)
    name = Column ( String(200), nullable = False)
    password = Column (Text, nullable =False)
    imageProfile = Column (Text, nullable = True)
    createdAt = Column(Text, nullable = True)
    email = Column (String(100), nullable = False)
    lastName = Column (String(200), nullable = False)
    dni = Column (Integer,nullable =False)
    phone = Column (Integer,nullable =False)
    tower = Column (Integer, nullable =False)
    dpto = Column (Integer, nullable =False)
    condominio = Column (String(500), nullable = False)

    def __init__(self, name,password,imageProfile,createdAt,email, lastName,dni,phone,tower,dpto,condominio) -> None:
        self.name = name
        self.password = password
        self.imageProfile = imageProfile
        self.createdAt = createdAt
        self.email = email
        self.lastName = lastName
        self.dni = dni
        self.phone = phone
        self.tower = tower
        self.dpto = dpto
        self.condominio = condominio
        
    def __str__(self) -> str: #metodo magico para no retorne UsuarioModel1 sino el nombre asignado
        return self.name

    def convertirJson (self):
        return {
            'id' : self.id,
            'name' : self.name,
            'createdAT':self.createdAt,
            'email' : self.email,
            'lastName' : self.lastName,
            'dni' : self.dni,
            'phone' : self.phone,
            'tower' : self.tower,
            'dpto' : self.dpto,
            'condominio' : self.condominio,
        }