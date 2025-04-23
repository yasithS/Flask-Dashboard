from application import app

@app.route("/")
def indeex():
    return "Hello, World!"