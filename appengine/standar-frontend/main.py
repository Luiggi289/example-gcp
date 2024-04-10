
# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request ,jsonify
import os

# [END imports]

server_url = os.environ.get('SERVER_URL')

if server_url is None :
   server_url = 'http://127.0.0.1:8090'



# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START form]
@app.route("/")
def form():
    return render_template("form.html")


# [END form]


# [START submitted]
@app.route("/submitted", methods=["POST"])
def submitted_form():
    name = request.form["name"]
    email = request.form["email"]
    document = request.form["document"]
    comments = request.form["comments"]

    # [END submitted]
    # [START render_template]
    return render_template(
        "submitted_form.html", name=name, email=email, document=document, comments=comments
    )
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500


# [END app]
if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8080, debug=True)