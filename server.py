import os
from flask import Flask, request, send_from_directory, render_template, redirect

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))


usuario_localizaciones = {}

@app.route('/actualizar_ubicacion', methods=['POST', 'OPTIONS'])
def actualizar_ubicacion():
    if request.method == 'POST':
        data = request.get_json()
        id_usuario = data['id_usuario']
        localizacion = data['localizacion']
        usuario_localizaciones['id_usuario'] = localizacion
        return "Ubicacion Actualizada"
        
    elif request.method == 'OPTIONS':
        return ("", 200)

@app.route('/obtener_ubicacion', methods=['GET'])
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
