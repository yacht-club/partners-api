import os

from api import create_app


from config import PORT


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
