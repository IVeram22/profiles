from flask import Flask
from app.configuration import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
