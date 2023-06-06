import logging
import os
from datetime import datetime

class Logger:
  def __init__(self, log_type, current_directory):
    # Create log folder if not exists
    if not os.path.exists(f"{current_directory}/logs/{datetime.now().strftime('%Y-%m-%d')}"):
      os.makedirs(f"{current_directory}/logs/{datetime.now().strftime('%Y-%m-%d')}")

    # Create log filename with current date
    log_filename = f"{current_directory}/logs/{datetime.now().strftime('%Y-%m-%d')}/{log_type}.log"

    # Create logger
    self.logger = logging.getLogger(log_type)
    self.logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)

    # Create formatter and add to file handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    self.logger.addHandler(file_handler)

  def log(self, message):
    self.logger.info(message)