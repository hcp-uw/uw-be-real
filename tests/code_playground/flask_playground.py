# File imports
import sys
from os.path import dirname, realpath

# Add src directory to path
current = dirname(realpath(__file__))
top = dirname(dirname(current))
sys.path.append(top)

# Flask imports
from flask import (
    Flask,
    request,
    jsonify,
)

# Custom class imports
from src.controller.api.user_network import UserNetwork
from src.controller.api.user_content import UserContent
from src.model.classes.env_loader import SECRETS


# Flask app
app = Flask(__name__)


def main():
    pass


if __name__ == "__main__":
    main()
