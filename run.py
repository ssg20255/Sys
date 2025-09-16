# run.py - entrypoint for the Flask app
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Development server; for production use WSGI server (gunicorn / uwsgi)
    app.run(host="0.0.0.0", port=5000, debug=True)