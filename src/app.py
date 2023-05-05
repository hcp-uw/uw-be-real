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

# Logger imports
from logging import (
    Logger,
    getLogger,
)

# Flask imports
from flask import (
    Flask,
    request,
    jsonify,
)
from flask_restful import (
    Resource,
    Api,
)
from flask_cors import CORS

# Service configuration imports
from src.config import ENV

# Model imports
from src.model.data_access.user_content import UserContent
from src.model.data_access.user_network import UserNetwork

# API resource imports
from src.controller.api_resources.user_create import UserCreate


def add_resources(
    api: Api, user_network: UserNetwork, user_content: UserContent
) -> None:
    api.add_resource(
        UserCreate,
        "/api/user-create",
        resource_class_kwargs={"user_network": user_network},
    )


def main():
    # Logger
    logger: Logger = getLogger()

    # App processes
    user_network: UserNetwork = UserNetwork(
        ENV.neo4j_creds,
    )
    user_content: UserContent = UserContent(
        ENV.s3_creds, ENV.mongo_uri, ENV.redis_creds
    )

    # Flask application
    app = Flask(__name__)
    api = Api(app)

    # Enable Cross Origin Resource Sharing
    CORS(app)

    # Add API endpoint Resources
    add_resources(api, user_network, user_content)

    # Run Flask application
    app.run(debug=True, port=5555)


if __name__ == "__main__":
    main()
