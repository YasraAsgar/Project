import os
import threading
from flask import Flask,send_file
from pyngrok import ngrok
os.environ["Flask_ENV"]="development"
app= Flask(__name__)
port=9000
ngrok.set_auth_token("2PyL4Rm5UR6dSSHniAQXeNwsVrJ_6TSbUxDm8dNdVfsHK26ch")
public_url=ngrok.connect(port).public_url
print("  * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format (public_url, port))
app.config["BASE_URL"]=public_url

@app.route("/")
def index():
  return send_file("app.py", as_attachment=True)

def run_flask_app():
    app.run(debug=True,port=5900)

threading.Thread(target=app.run,kwargs={"use_reloader":False}).start()
