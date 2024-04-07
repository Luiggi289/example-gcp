from flask import Flask, request,jsonify
from google.cloud import firestore
from datetime import datetime
import pytz
import os
from flask_cors import CORS

PROJECT_ID= 'tensile-impact-412116'
URL_FRONTEND = os.environ.get('URL_FRONTEND')

if URL_FRONTEND is None :
   URL_FRONTEND = 'http://127.0.0.1:8080'

app = Flask(__name__)
#CORS(app, origins='http://127.0.0.1:8080')
CORS(app, origins=URL_FRONTEND)




@app.route("/")
def hello():
    return "Hola Mundo GCP!!"


@app.route('/card',methods=['POST'])
def create_delivered():
    req=request.get_json()

     # Obtener la fecha actual con la zona horaria de Perú
    zona_horaria_peru = pytz.timezone('America/Lima')
    fecha_actual_peru = datetime.now(zona_horaria_peru)

    # Conexión a Firestore
    db = firestore.Client(project=PROJECT_ID)

    # Referencia a la colección donde deseas guardar los datos
    coleccion = db.collection('card')

    req=request.get_json()
    datos={
        "name":req.get('name'),
        "email":req.get('email'),
        "document":req.get('document'),
        "comments":req.get('comments'),
        "card":req.get('card'),
        "created_datetime":fecha_actual_peru
    }



    # Agrega los datos a la colección
    coleccion.add(datos)

    return jsonify({"response":"success"}) ,201


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8090, debug=True)
