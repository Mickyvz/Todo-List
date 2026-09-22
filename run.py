from todor import create_app

if __name__ == '__main__': # Verifica si el script se está ejecutando directamente
    app = create_app() # Crea una instancia de la aplicación llamando a la función create_app() definida en todor/__init__.py
    app.run()