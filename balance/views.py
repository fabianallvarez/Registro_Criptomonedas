from . import app


@app.route("/")
def inicio():
    return "Pagina de inicio"


@app.route("/Compras", methods=["GET", "POST"])
def nuevo():
    return "Crear Compras"

@app.route("/Estado", methods=["GET", "POST"])
def actualizar():
    return "Actualizar Estado"

@app.route("/borrar", methods=["GET", "POST"])
def eliminar():
    return "Eliminar movimiento"