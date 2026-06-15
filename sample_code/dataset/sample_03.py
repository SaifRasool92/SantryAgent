import os
def get_env_var(key):
    return os.getenv(key, "default")
