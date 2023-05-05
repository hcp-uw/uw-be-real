from dotenv import load_dotenv
from os import (
    listdir,
    getcwd,
    getenv,
)
from os.path import join


class Config:
    """Config is a Singleton class that loads all of the necessary
    secret .env variables for the application services."""

    def __new__(cls) -> None:
        """Ensures Singleton design pattern."""
        if not hasattr(cls, "instance"):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        """Instantiates and stores .env variables."""
        # Load credentials
        credentials: tuple[dict, dict, dict, dict] = self._load_env()

        # Destruct tuple
        self.aws_s3: dict = credentials[0]
        self.mongodb: dict = credentials[1]
        self.neo4j: dict = credentials[2]
        self.redis: dict = credentials[3]

        # UserNetwork-compatible data
        self.neo4j_creds: tuple[str, str, str] = (
            self.neo4j["uri"],
            self.neo4j["username"],
            self.neo4j["password"],
        )

        # UserContent-compatible data
        self.s3_creds: tuple[str, str] = (
            self.aws_s3["access_key"],
            self.aws_s3["secret_access_key"],
        )
        self.mongo_uri: str = self.mongodb["uri"]
        self.redis_creds: tuple[str, str, str] = (
            self.redis["host"],
            self.redis["port"],
            self.redis["password"],
        )

    def _load_env(self) -> tuple[dict, dict, dict, dict]:
        """Loads env variables and returns a tuple of dict for
        (aws_s3, mongodb, neo4j, redis) credentials."""
        # Load env variables
        secrets_path = join(getcwd(), "secrets")
        for env_path in listdir(secrets_path):
            load_dotenv(join(secrets_path, env_path, ".env"))

        aws_s3: dict = {
            "access_key": getenv("ACCESS_KEY"),
            "secret_access_key": getenv("SECRET_ACCESS_KEY"),
        }
        mongodb: dict = {
            "uri": getenv("MONGODB_URI"),
        }
        neo4j: dict = {
            "uri": getenv("NEO4J_URI"),
            "username": getenv("NEO4J_USERNAME"),
            "password": getenv("NEO4J_PASSWORD"),
        }
        redis: dict = {
            "host": getenv("REDIS_HOST"),
            "port": getenv("REDIS_PORT"),
            "password": getenv("REDIS_PASSWORD"),
        }

        return aws_s3, mongodb, neo4j, redis


ENV = Config()
