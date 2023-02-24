# Crear un entorno virtual
```
python -m venv venv
```
# Actuvar el entorno virtual
```
venv\Scripts\activate (alt+92)
source venv/Scripts/activate
source venv/bin/activate
```
# Instalar Flask
```
pip install flask
```
# Correr la apliacion de Flask
```
flask --debug run
```
# Instalar SQLAlchemy
```
pip install Flask-SQLAlchemy
```
# Registar las librerias y dependencias instaladas
```
pip freeze > requirements.txt
```
# Creamos los modelos 
```
productos_model.py
```
# Creamos los controladores 
```
productos_controller.py
```
# Creamos las rutas
```
productos_router.py
```
# Migrar la base de datos
```
pip install Flask-Migrate
```
# Crear la carpeta Migrations
```
1. flask db init
2. flask db migrate -m "first migration"
3. flask db upgrade
```
