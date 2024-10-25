# analytics/logger.py
import logging

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_request(endpoint: str, method: str):
    logging.info(f"Request to {endpoint} with method {method}")
