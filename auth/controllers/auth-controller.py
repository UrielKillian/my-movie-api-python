import main


@main.app.get("/auth")
def auth():
    return "Hello World"