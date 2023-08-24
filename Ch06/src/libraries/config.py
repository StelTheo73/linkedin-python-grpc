""" Configuration module """

from os import environ as env

PORT = int(env.get("PORT", 8888))
HOST = env.get("HOST", "localhost")

CERT_FILE = env.get("CERT_FILE", "cert.pem")
KEY_FILE = env.get("KEY_FILE", "key.pem")
