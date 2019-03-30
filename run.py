from api import create_app

from config import PORT


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=PORT, debug=True)