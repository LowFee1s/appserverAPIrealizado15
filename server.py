import os
from flask_httpauth import HTTPBasicAuth
from flask import Flask, request, jsonify, send_from_directory, render_template, redirect

app = Flask(__name__)
auth = HTTPBasicAuth()




USER_DATA = {



    
    "apprastreoadministracionproyectorealizado": os.environ.get("CLAVE")




}




port = int(os.environ.get("PORT", 5000))




usuario_localizaciones = {}

@auth.verify_password
def verificar(username, password):
    if not (username and password): 
        return False
    return USER_DATA.get(username) == password

@app.route('/update_ubicacion', methods=['POST', 'OPTIONS'])
@auth.login_required
def update_ubicacion():
    if request.method    ==    'POST':
        data = request.get_json()
        id_usuario = data['id_usuario']
        localizacion = data['localizacion']
        usuario_localizaciones[id_usuario] = localizacion
        return "Ubicacion Actualizada"
        
    elif request.method    ==    'OPTIONS':
        return ("", 200)

@app.route('/obtener_ubicacion', methods=['GET'])
@auth.login_required
def obtener_ubicacion():
        return usuario_localizaciones




@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)











































































