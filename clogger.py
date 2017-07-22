#!/usr/bin/python

import logging
import logging.handlers
import os
import sys
from colorlog import ColoredFormatter
import argparse

class ColorLogger(object):
    """docstring for ClassName"""
    def __init__(self, loggerName, logLevel):
        super(ColorLogger, self).__init__()
        self.name = loggerName
        self.logLevel = logLevel
        self.log = logging.getLogger(self.name)

        self.log.setLevel(logging.DEBUG)
        self.log.propagate = 0

        # create formatters
        consoleFormatter = ColoredFormatter("  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s")
        syslogFormater = logging.Formatter("%(name)s[%(process)d]: %(levelname)s - %(message)s")

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, self.logLevel))
        console_handler.setFormatter(consoleFormatter)

        # create syslog handler
        # and set its log level to DEBUG
        #
        file_handler = logging.handlers.SysLogHandler(address='/dev/log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(syslogFormater)

        # add handlers to the "mypackage" logger
        self.log.addHandler(console_handler)
        self.log.addHandler(file_handler)

    def debug(self, message):
        self.log.debug(message)

    def info(self, message):
        self.log.info(message)

    def warn(self, message):
        self.log.warn(message)

    def error(self, message):
        self.log.error(message)

    def fatal(self, message):
        self.log.fatal(message)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tag", type=str, default="colorlog")
parser.add_argument("-l", "--level", type=str, default="INFO")
args = parser.parse_args()

logger = ColorLogger(args.tag, "DEBUG")
for line in sys.stdin.readlines():
    if args.level == "DEBUG" or args.level == "DEB":
        logger.debug(line.rstrip())
    elif args.level == "INFO":
        logger.info(line.rstrip())
    elif args.level == "WARNING" or args.level == "WARN":
        logger.warn(line.rstrip())
    elif args.level == "ERROR" or args.level == "ERR":
        logger.error(line.rstrip())
    elif args.level == "FATAL" or args.level == "CRIT" or args.level == "CRITICAL":
        logger.fatal(line.rstrip())
    else:
        logger.info(line.rstrip())

