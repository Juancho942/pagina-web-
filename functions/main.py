# functions/main.py

from flask import Flask, render_template
from datetime import datetime
from firebase_functions import https_fn
import firebase_admin
from firebase_admin import credentials, db
import os

# --- CONEXIÓN A FIREBASE (VERSIÓN FINAL Y ROBUSTA) ---
# Se inicializa la app con la URL explícita para asegurar la conexión en la nube.
if os.environ.get('GCP_PROJECT'):
    if not firebase_admin._apps:
        firebase_admin.initialize_app({
            'databaseURL': 'https://pagina-web-6fb65-default-rtdb.firebaseio.com'
        })
# ----------------------------------------------------

# --- RUTA ABSOLUTA A PLANTILLAS ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
flask_app = Flask(__name__, template_folder=TEMPLATE_DIR)
# ----------------------------------


# --- El resto del código ---
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
color_palette = {
    'primary': '#f7bec8', 'dark_1': '#c7919e', 'dark_2': '#a0606e',
    'dark_3': '#6e3b46', 'white': '#FFFFFF', 'light_gray': '#f9fafb'
}

@flask_app.context_processor
def inject_global_vars():
    return {
        'aktuellen_Datum': datetime.utcnow(),
        'brand': brand_info,
        'colors': color_palette
    }

def get_products_from_db():
    if not firebase_admin._apps:
        return {}
    try:
        ref = db.reference('/inventario')
        products = ref.get()

        if not products: return {}

        products_by_category = {}
        for key, product_data in products.items():
            # --- LÍNEA MODIFICADA ---
            # Ahora solo verificamos que el producto tenga una categoría, sin filtrar por stock.
            if isinstance(product_data, dict) and 'categoria' in product_data:
            # --------------------------
                category = product_data['categoria'].strip().upper()
                if category not in products_by_category:
                    products_by_category[category] = []
                products_by_category[category].append(product_data)
        return products_by_category
    except Exception as e:
        print(f"Error al obtener datos de Firebase: {e}")
        return {}

@flask_app.route('/')
def index():
    """ La página principal ES LA TIENDA. """
    products_by_category = get_products_from_db()
    return render_template('tienda.html', products_by_category=products_by_category)

@flask_app.route('/informacion')
@flask_app.route('/QR')
def informacion():
    """ Esta ruta es la página de contacto. """
    return render_template('informacion.html')

@https_fn.on_request(max_instances=1)
def mi_aplicacion_flask(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response.from_app(flask_app, req)