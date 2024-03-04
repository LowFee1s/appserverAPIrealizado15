
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
camiones = set()


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
        ruta = data.get('Ruta', [])
        tipo = data['Tipo']
        direccion = data['Direccion']
        camion = data.get('Camion', '')
        camiones.add(camion)

        usuario_localizaciones[id_usuario] = {
            'localizacion': localizacion,
            'Ruta': ruta,
            'Direccion': direccion,
            'Tipo': tipo,
            'Camion': camion,
        }

        return "Ubicacion Actualizada"
        
    elif request.method    ==    'OPTIONS':
        return ("", 200)
        
@app.route('/obtener_ubicacion/<camion>', methods=['GET'])
@auth.login_required
def obtener_ubicacion_camion(camion):
    datos_camion = {k: v for k, v in usuario_localizaciones.items() if v['Camion'] == camion}
    return datos_camion

@app.route('/obtener_ubicacion_tipo/<tipo>', methods=['GET'])
@auth.login_required
def obtener_ubicacion_tipo(tipo):
    dato_tipo = {k: v for k, v in usuario_localizaciones.items() if v['Tipo'] == tipo}
    return dato_tipo

@app.route('/camiones', methods=['GET'])
@auth.login_required
def mostrar_camiones():
    return list(camiones)

@app.route('/quitar_ubicacion', methods=['POST', 'OPTIONS'])
@auth.login_required
def quitar_ubicacion():
    if request.method    ==    'POST':
        data = request.get_json()
        id_usuario = data['id_usuario']
        if id_usuario in usuario_localizaciones:
            del usuario_localizaciones[id_usuario]
        return "Ubicacion Quitada"
        
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











































































