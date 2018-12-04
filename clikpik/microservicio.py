from flask import Flask
from os import environ
import json
from flask import request
from flask_sqlalchemy import SQLAlchemy
app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['TESTING'] = True
db = SQLAlchemy(app)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    ubicacion = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/nuevoproducto/<nombre>/<ubicacion>', methods=['POST'])
def nuevousuario(nombre,ubicacion):
    producto = Producto(nombre=nombre, ubicacion=ubicacion)
    db.session.add(producto)
    db.session.commit()
    return "nuevousuario"


@app.route('/')
def raiz():
    return json.dumps({
   "status": "OK",
   "ejemplo": { "ruta": "/productos",
                "valor": [{"nombre": "producto3", "id": 1, "ubicacion": "ubicacion3"}]
              }
})


@app.route('/productos', methods=['GET','PUT', 'POST', 'DELETE'])
def productos():
    if request.method == 'GET':
        todo= Producto.query.all()
        resultado = []
        for item in todo:
            temp = item.__dict__
            del temp["_sa_instance_state"]
            resultado.append(temp)
        return json.dumps(resultado)
    elif request.method == 'PUT':
        producto = Producto(nombre=request.json['nombre'], ubicacion=request.json['ubicacion'])
        db.session.add(producto)
        db.session.commit()
        return "nuevousuario"

@app.route('/initdb')
def initdb():
    db.create_all()
    return "Base de datos iniciada"
