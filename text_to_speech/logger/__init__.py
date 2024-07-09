import logging
import os
from datetime import datetime


# Create log directory
LOG_DIR = "pylogs"
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)


# Create log directory USING log directory
os.makedirs(LOG_DIR, exist_ok=True)

# Create logfile name
CURRENT_TIME_STAMP = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
file_name = f'log_{CURRENT_TIME_STAMP}'
log_file_path = os.path.join(LOG_DIR, file_name)

# Configure logging
logging.basicConfig(filename=log_file_path, 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s =======> %(message)s',
                    datefmt="%d-%m-%Y %H:%M")

# Create Object for Logging
logger = logging.getLogger()