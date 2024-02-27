import logging

def configure_logging():
    logging.basicConfig(
        filename='activity.log',  # Log file
        level=logging.DEBUG,      # Log level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format with timestamp
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format for timestamp
    )
