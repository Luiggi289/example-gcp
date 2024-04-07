
# [START app]

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
    return render_template("form.html",server_url=server_url)


# [END form]





# [END app]
if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8080, debug=True)