from flask import Flask
from api.routes import setup_routes

app = Flask(__name__)

if __name__ == '__main__':
    setup_routes(app)
    app.run(debug=True, host='0.0.0.0', port=5000)
