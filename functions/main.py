# functions/main.py
from flask import Flask, render_template # Asegúrate que render_template esté importado
from datetime import datetime
from firebase_functions import https_fn # Necesario para Cloud Functions

# Nombre de la instancia de Flask.
# Flask buscará la carpeta 'templates' en el mismo directorio que este archivo (functions/templates/).
flask_app = Flask(__name__)

# Paleta de colores
color_palette = {
    'primary': '#f7bec8',
    'dark_1': '#c7919e',
    'dark_2': '#a0606e',
    'dark_3': '#6e3b46',
    'white': '#FFFFFF',
    'light_gray': '#f9fafb'
}

# Información de la marca
brand_info = {
    'name': 'Francely Accesorios',
    'domain': 'www.francelyaccesorios.com',
    'address': 'Cra 3 # 13 - 19 Local 2, Cartago, Colombia',
    'hours': 'Lunes a Sábado: 10:00 AM - 7:00 PM',
    'history': 'Francely Accesorios nace en Cartago, Colombia, como una marca de joyería exclusiva que celebra la belleza natural de cada mujer. Nos especializamos en aretes, anillos, collares y accesorios bañados en oro, hechos a mano con detalle y dedicación. Nuestros diseños están pensados para toda mujer que desea destacar con elegancia y sofisticación.',
    'cta': 'Síguenos en redes y visítanos para conocer lo nuevo que tenemos para ti.',
    'social_links': {
        'instagram': 'https://www.instagram.com/francelyvalenciaaccesorios',
        'whatsapp': 'https://wa.me/573053789268',
        'tiktok': 'https://www.tiktok.com/@francelyaccesorios'
    }
}

@flask_app.context_processor
def inject_global_vars():
    """ Inyecta variables globales en todas las plantillas """
    return {
        'aktuellen_Datum': datetime.utcnow(),
        'brand': brand_info,
        'colors': color_palette
    }

@flask_app.route('/')
def index():
    """
    Ruta principal que muestra la página "Próximamente" o la página de inicio.
    """
    # Si 'index.html' es tu página "Próximamente", está bien.
    # Si tienes otra página de inicio, cambia el nombre de la plantilla aquí.
    return render_template('index.html')

@flask_app.route('/informacion')
@flask_app.route('/QR') # Ambas rutas llevan a la misma página
def informacion():
    """
    Ruta para la página de información/QR.
    """
    return render_template('informacion.html')

# Esta es la Cloud Function que Firebase desplegará.
# El nombre 'mi_aplicacion_flask' debe coincidir con el usado en firebase.json (rewrites).
@https_fn.on_request(max_instances=1) # Puedes ajustar max_instances según necesites
def mi_aplicacion_flask(req: https_fn.Request) -> https_fn.Response:
    """
    Punto de entrada para Firebase Functions. Todas las solicitudes HTTP
    dirigidas a esta función serán manejadas por la aplicación Flask.
    """
    # Pasa la solicitud HTTP a tu aplicación Flask.
    # La biblioteca firebase_functions maneja la adaptación WSGI necesaria.
    return https_fn.Response.from_app(flask_app, req)

# NO INCLUYAS:
# if __name__ == '__main__':
# flask_app.run(debug=True)
# Firebase se encarga de iniciar el servidor.