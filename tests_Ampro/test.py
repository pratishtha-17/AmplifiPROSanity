import logging

logging.basicConfig(filename="log.txt",format='%(asctime)s: %(levelname)s: %(message)s',
datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
logging.warning("Warning")
logging.warning("Info")
logging.warning("Error")

