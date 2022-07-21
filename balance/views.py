from . import app


@app.route("/")
def inicio():
    return "Pagina de inicio"


@app.route("/Compras", methods=["GET", "POST"])
def nuevo(id):
    return f"Crear Compras"

@app.route("/Estado/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    return f"Actualizar Estado con el ID={id}"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    return f"Eliminar el movimiento {id}"