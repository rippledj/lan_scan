# LanScanLogger.py
# Lan Scan - Processes for Managing Logs
# Description: Processes handles log files.
# Author: Joseph Lee
# Email: joseph@ripplesoftware.ca
# Website: www.ripplesoftware.ca
# Github: www.github.com/rippledj/lan_scan

# Import Python Modules
import logging
from pathlib import Path
import traceback
import time
import os
import sys
import pprint

# Setup logging
def setup_logger(log_level, log_file):

    # Create the log file if not exists
    if not os.path.exists(log_file): Path(log_file).touch()

    # Define logger object
    logger = logging.getLogger('LanScan_Logs')
    log_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    # Set the log level verbosity
    if log_level == 1:
        logger.setLevel(logging.ERROR)
    elif log_level == 2:
        logger.setLevel(logging.WARNING)
    elif log_level == 3:
        logger.setLevel(logging.INFO)
