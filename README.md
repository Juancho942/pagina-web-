
# Sitio Web Francely Accesorios

Este es el proyecto del sitio web para Francely Accesorios, desarrollado con Flask y Tailwind CSS.

## Requisitos Previos

- Python 3.x
- Node.js y npm (o yarn)

## Configuración del Entorno

1.  **Clona o crea los archivos del proyecto:**
    Asegúrate de tener la estructura de carpetas y todos los archivos como se describe.

2.  **Crea un entorno virtual para Python (recomendado):**
    ```bash
    python -m venv venv
    ```
    Actívalo:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`

3.  **Instala las dependencias de Python:**
    ```bash
    pip install Flask
    ```

4.  **Instala las dependencias de Node.js (para Tailwind CSS):**
    Navega a la raíz del proyecto (`francely_accesorios/`) en tu terminal y ejecuta:
    ```bash
    npm install
    ```

## Ejecución del Proyecto

Necesitarás dos terminales abiertas en la raíz del proyecto (`francely_accesorios/`).

1.  **Terminal 1: Compilar Tailwind CSS:**
    Ejecuta el siguiente comando para que Tailwind observe los cambios en tus archivos HTML y `input.css`, y genere `static/css/style.css`:
    ```bash
    npm run dev
    ```

2.  **Terminal 2: Ejecutar la Aplicación Flask:**
    Asegúrate de que tu entorno virtual de Python esté activado y luego ejecuta:
    ```bash
    python app.py
    ```

3.  **Abre tu navegador:**
    Ve a `http://127.0.0.1:5000/` para ver la página principal.
    Ve a `http://127.0.0.1:5000/informacion` (o `/QR`) para la página de información.

## Estructura del Proyecto

-   `app.py`: Archivo principal de la aplicación Flask.
-   `static/`: Contiene archivos estáticos.
    -   `css/input.css`: Archivo fuente de CSS para Tailwind.
    -   `css/style.css`: Archivo CSS generado por Tailwind (no incluir en control de versiones si se genera en cada build).
    -   `images/`: Para imágenes como el logo.
-   `templates/`: Contiene las plantillas HTML de Jinja2.
-   `tailwind.config.js`: Archivo de configuración para Tailwind CSS.
-   `package.json`: Define las dependencias de Node.js y scripts.

## Notas

-   Reemplaza `static/images/logo.png` con el logo real de Francely Accesorios.
-   Actualiza los enlaces de redes sociales en `app.py` en el diccionario `brand_info`.
-   Para producción, ejecuta `npm run build` para minificar el CSS y considera un servidor WSGI como Gunicorn
