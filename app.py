from flask import Flask, render_template
from datetime import datetime # Para el año actual en el footer

app = Flask(__name__)

# Paleta de colores para pasar a las plantillas (opcional, pero puede ser útil)
# Se usarán principalmente clases de Tailwind, pero esto es para referencia.
color_palette = {
    'primary': '#f7bec8',
    'dark_1': '#c7919e',
    'dark_2': '#a0606e',
    'dark_3': '#6e3b46',
    'white': '#FFFFFF',
    'light_gray': '#f9fafb' # Un gris muy claro para fondos suaves
}

# Información de la marca
brand_info = {
    'name': 'Francely Accesorios',
    'domain': 'www.francelyaccesorios.com',
    'address': 'Cartago, Colombia', # Sé más específico si lo deseas
    'hours': 'Lunes a Sábado: 10:00 AM - 7:00 PM', # Ajusta según sea necesario
    'history': 'Francely Accesorios nace en Cartago, Colombia, como una marca de joyería exclusiva que celebra la belleza natural de cada mujer. Nos especializamos en aretes, anillos, collares y accesorios bañados en oro, hechos a mano con detalle y dedicación. Nuestros diseños están pensados para toda mujer que desean destacar con elegancia y sofisticación.',

    'cta': 'Síguenos en redes y visítanos para conocer lo nuevo que tenemos para ti.',
    'social_links': {
        'instagram': 'https://www.instagram.com/francelyvalenciaaccesorios', # Reemplaza con el enlace real
        'whatsapp': 'https://wa.me/573053789268', # Reemplaza con tu número de WhatsApp (formato internacional)
        'tiktok': 'https://www.tiktok.com/@francelyaccesorios' # Reemplaza con el enlace real
    }
}

@app.context_processor
def inject_current_date():
    """ Inyecta la fecha actual en las plantillas """
    return {'aktuellen_Datum': datetime.utcnow()}


@app.route('/')
def index():
    """
    Ruta principal que muestra la página "En construcción".
    """
    return render_template('index.html', colors=color_palette, brand=brand_info)

@app.route('/informacion')
@app.route('/QR') # Ambas rutas llevan a la misma página
def informacion():
    """
    Ruta para la página de información/QR.
    """
    return render_template('informacion.html', colors=color_palette, brand=brand_info)

if __name__ == '__main__':
    app.run(debug=True)