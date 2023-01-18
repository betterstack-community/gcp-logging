from google.cloud import logging
from datetime import datetime
import time


logging_client = logging.Client()
logger = logging_client.logger("demo-log")

while True:
    logger.log_struct(
        {"message": "Request made.", "key": "value", "num": 12}, severity="DEBUG"
    )
    time.sleep(1)
    logger.log_struct(
        {"message": "A user has logged in.", "username": "testuser"}, severity="INFO"
    )
    time.sleep(1)
    logger.log_struct({"message": "Low disk space.", "size": 25}, severity="WARNING")
    time.sleep(1)
    logger.log_struct(
        {"message": "Error connecting to database.", "dbname": "maindb"},
        severity="ERROR",
    )
    time.sleep(1)
    logger.log_struct(
        {"message": "Application crashed.", "code": 12345}, severity="CRITICAL"
    )
    time.sleep(1)
