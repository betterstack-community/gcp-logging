from google.cloud import logging
from flask import Flask, render_template
import random

app = Flask(__name__)

logging_client = logging.Client()
logger = logging_client.logger("demo-log")


@app.route("/")
def hello_world():
    for i in range(20):
        logger.log_struct(
            {"message": "Request made.", "key": "value", "num": random.randint(0,50)}, severity="DEBUG"
        )
        logger.log_struct(
            {"message": "A user has logged in.", "username": "testuser"}, severity="INFO"
        )
        logger.log_struct({"message": "Low disk space.", "size": random.randint(0,100)}, severity="WARNING")
        logger.log_struct(
            {"message": "Error connecting to database.", "dbname": "maindb"},
            severity="ERROR",
        )
        logger.log_struct(
            {"message": "Application crashed.", "code": random.randint(1111,9999)}, severity="CRITICAL"
        )
    return render_template("index.html")
