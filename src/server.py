import sys
from json import dumps
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from src.error import InputError
from src import config


if __name__ == "__main__":
    APP.run(port=config.port) # Do not edit this port
