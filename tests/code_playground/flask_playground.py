# File imports
import sys
from os.path import (
    dirname,
    realpath,
)

# Add src directory to path
current = dirname(realpath(__file__))
top = dirname(dirname(current))
sys.path.append(top)

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

# Custom class imports
from src.model.data_access.user_content import UserContent
from src.model.data_access.user_network import UserNetwork
from src.config import ENV

# API endpoint imports
from tests.code_playground.upload_image import UploadImage


def add_resources(
    api: Api, user_network: UserNetwork, user_content: UserContent
) -> None:
    api.add_resource(
        UploadImage,
        "/api/upload-image",
        resource_class_kwargs={
            "user_network": user_network,
            "user_content": user_content,
        },
    )


def main():
    # Logger
    logger: Logger = getLogger()

    # App processes
    user_network: UserNetwork = UserNetwork(ENV.neo4j_creds)
    user_content: UserContent = UserContent(
        ENV.s3_creds, ENV.mongo_uri, ENV.redis_creds
    )

    # Flask application
    app = Flask(__name__)
    api = Api(app)

    # Add API endpoint Resources
    add_resources(api, user_network, user_content)

    # Run Flask application
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
