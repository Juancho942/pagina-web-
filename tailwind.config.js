/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Escanea todos los archivos HTML en la carpeta templates
    "./static/src/**/*.js",   // Si tienes JS que manipula clases de Tailwind
  ],
  theme: {
    extend: {
      colors: {
        'brand-primary': '#f7bec8',
        'brand-dark-1': '#c7919e',
        'brand-dark-2': '#a0606e',
        'brand-dark-3': '#6e3b46',
        'brand-white': '#FFFFFF',
        'brand-light-gray': '#f9fafb', // Un gris muy claro para fondos
        'brand-text': '#5c5c5c', // Un gris oscuro para texto principal
        'brand-text-light': '#7b7b7b', // Un gris más claro para texto secundario
      },
      fontFamily: {
        'sans': ['Montserrat', 'sans-serif'], // Fuente para cuerpo de texto
        'serif': ['Playfair Display', 'serif'], // Fuente para títulos
      },
    },
  },
  plugins: [],
}