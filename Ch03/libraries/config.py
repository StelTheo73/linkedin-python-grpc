""" Configuration module """

from os import environ as env

PORT = int(env.get("PORT", 8888))
HOST = env.get("HOST", "localhost")
