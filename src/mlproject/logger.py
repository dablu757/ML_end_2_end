import logging
import os
from datetime import datetime

#create log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#create log folder
LOG_FOLDER = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(LOG_FOLDER,exist_ok=True)


#complete log path
LOG_FILE_PATH = os.path.join(LOG_FOLDER,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)