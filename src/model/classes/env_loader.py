from dotenv import load_dotenv
from os import listdir, getcwd, getenv
from os.path import join


class EnvLoader:
    """EnvLoader is a classic Singleton class that loads all of the necessary
    secret .env variables for UserContent and UserNetwork."""

    def __new__(cls) -> None:
        """Ensures Singleton design pattern."""
        if not hasattr(cls, "instance"):
            cls.instance = super(EnvLoader, cls).__new__(cls)
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

    def _load_env(self) -> tuple[dict, dict, dict, dict]:
        """Loads env variables and returns a tuple of dict for
        (aws_s3, mongodb, neo4j, redis) credentials."""
        # Load env variables
        for env_path in listdir(join(getcwd(), "secrets")):
            load_dotenv(join(env_path, ".env"))

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


SECRETS = EnvLoader()
