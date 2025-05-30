import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

logging.info("Program started")
try:
    x = 5 / 0
except Exception as e:
    logging.error("Error occurred: %s", e)
