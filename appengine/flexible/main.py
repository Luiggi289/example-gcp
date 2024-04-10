from flask import Flask , jsonify


app = Flask(__name__)


# [START example]
@app.route("/")
def home():
    return "Hola Mundo"

# [END example]



if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See CMD in Dockerfile.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END app]
