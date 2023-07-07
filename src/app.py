# File imports
import sys
from os.path import (
    dirname,
    realpath,
)

# add src directory to path
current = dirname(realpath(__file__))
parent = dirname(current)
sys.path.append(parent)

# Flask imports
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# App setup import
from src import setup


# Flask application set up
app: Flask = Flask(__name__)
api: Api = Api(app)

# Enable Cross Origin Resource Sharing
CORS(app)

# Set up modules and resources for Flask app
setup.setup(api)


def main() -> None:
    # Run Flask application
    # app.run(debug=True, host="0.0.0.0")  # For Docker container
    app.run(debug=True, port=5000)  # For local testing


if __name__ == "__main__":
    main()
