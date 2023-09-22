# Logger imports
from logging import (
    Logger,
    getLogger,
)

# Flask imports
from flask_restful import Api
from controller.api_resources.friend_request_get import FriendRequestGet
from controller.api_resources.friend_request_send import FriendRequestSend

# Model imports
from src.model.data_access.user_content import UserContent
from src.model.data_access.user_network import UserNetwork

# API resource imports
from src.controller.api_resources.user_create import UserCreate
from src.controller.api_resources.user_profile import UserProfile
from src.controller.api_resources.post_create import PostCreate
from src.controller.api_resources.friend_get import FriendGet

# Service configuration imports
from src.config import ENV


def add_resources(
    api: Api,
    user_network: UserNetwork,
    user_content: UserContent,
    logger: Logger,
) -> None:
    """Adds API endpoints to the Flask application."""
    api.add_resource(
        UserCreate,
        "/api/user-create",
        resource_class_kwargs={"user_network": user_network, "logger": logger},
    )
    api.add_resource(
        UserProfile,
        "/api/user-profile",
        resource_class_kwargs={"user_network": user_network, "logger": logger},
    )
    api.add_resource(
        PostCreate,
        "/api/post-create",
        resource_class_kwargs={"user_network": user_network, "logger": logger, "user_content": user_content}
    )
    api.add_resource(
        FriendGet,
        "/api/friend-get",
        resource_class_kwargs={"user_network": user_network, "logger": logger},
    )
    api.add_resource(
        FriendRequestSend,
        "/api/friend-request-send",
        resource_class_kwargs={"user_network": user_network, "logger": logger},
    )
    api.add_resource(
        FriendRequestGet,
        "/api/friend-request-get",
        resource_class_kwargs={"user_network": user_network, "logger": logger}
    )


def setup(api: Api) -> None:
    """Sets up the Flask application."""
    # Initialize relevant modules
    user_network: UserNetwork = UserNetwork(
        ENV.neo4j_creds,
    )
    user_content: UserContent = UserContent(
        ENV.s3_creds, ENV.mongo_uri, ENV.redis_creds
    )
    logger: Logger = getLogger()

    # Add API endpoint Resources
    add_resources(api, user_network, user_content, logger)
