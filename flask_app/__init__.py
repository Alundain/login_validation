from flask import Flask 
#from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key="secretKey" # se necesita para la sesión
#bcrypt = Bcrypt(app)
