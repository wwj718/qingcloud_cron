#!/usr/bin/env python
# encoding: utf-8

import logging
import logging.handlers

LOG_FILE = 'qingcloud_cron.log'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler

handler = logging.FileHandler(LOG_FILE)
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

