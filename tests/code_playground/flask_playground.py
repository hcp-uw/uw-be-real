# File imports
import sys
from os import getcwd, getenv, listdir
from os.path import dirname, realpath, join
from dotenv import load_dotenv

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


# Load env variables
for env_path in listdir(join(getcwd(), "secrets")):
    load_dotenv(join(env_path, ".env"))

ENV = {
    "aws_s3": {
        "access_key": getenv("ACCESS_KEY"),
        "secret_access_key": getenv("SECRET_ACCESS_KEY"),
    },
    "mongodb": {
        "uri": getenv("MONGODB_URI"),
    },
    "neo4j": {
        "uri": getenv("NEO4J_URI"),
        "username": getenv("NEO4J_USERNAME"),
        "password": getenv("NEO4J_PASSWORD"),
    },
    "redis": {
        "host": getenv("REDIS_HOST"),
        "port": getenv("REDIS_PORT"),
        "password": getenv("REDIS_PASSWORD"),
    },
}


# Flask app
app = Flask(__name__)


def main():
    pass


if __name__ == "__main__":
    main()
