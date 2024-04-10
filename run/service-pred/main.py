import tensorflow as tf
from flask import Flask , jsonify


app = Flask(__name__)


# [START example]
@app.route("/")
def home():
    return "Servicio de Predicciones"

@app.route('/predict/income/<int:p_income>',methods=['GET'])
def prdecit(p_income):
# Cargar el modelo de la red neuronal
    dnn_model = tf.keras.models.load_model("modelo.keras")

    # Datos de entrada 
    new_data = [[p_income]]  

    # Convertir los datos de entrada a tensores de TensorFlow
    new_data_tensor = tf.constant(new_data, dtype=tf.float32)

    # Realizar la predicción utilizando el modelo de la red neuronal
    prediction = dnn_model.predict(new_data_tensor)
    

    return jsonify( { "purchase" : float(prediction[0,0]) })


# [END example]



if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See CMD in Dockerfile.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END app]
