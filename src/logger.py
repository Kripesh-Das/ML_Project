import logging
import os
from datetime import datetime

# Generate a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the full path for the log file inside a "logs" directory in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the "logs" directory exists, create it if it doesn't
os.makedirs(logs_path, exist_ok=True)

# Define the complete path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    # Set the log file path
    filename=LOG_FILE_PATH,
    
    # Define the log message format
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    # Set the logging level to INFO
    level=logging.INFO,
)

# Example of logging a message
logging.info("Logging setup complete.")

