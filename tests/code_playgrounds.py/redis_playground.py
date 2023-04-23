import os
from dotenv import load_dotenv

import redis 

# load secrets
redis_env_path = os.path.join(os.getcwd(), 'secrets', 'redis', '.env')
load_dotenv(redis_env_path)

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')
password = os.getenv('REDIS_PASSWORD')

r = redis.Redis(host=host, port=port, password=password)

# r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(r.get("Bahamas"))