#Logging: is the process of recording information about what a program is doing while it runs. print() isn’t really designed for proper application monitoring or debugging. Instead, Python provides the logging system.
# Logging allows us to record things such as:
# * what the program is doing
# * whether something went wrong
# * warnings
# * errors
# * debugging information
# * when something happened
# * where something happened

# Reason 1 — Debugging
# Reason 2 — Finding errors
# Reason 3 — Monitoring programs
# Reason 4 — Understanding program flow
# Reason 5 — Logs can be saved >>> logging can send msgs to the terminal or save them in a file

import logging

# basicConfig() is Python’s shortcut to set up the default logging system. It configures the root logger with a handler, formatter, and severity threshold.
# Without configuration, Python uses default logging behavior.
# But we often want to tell logging:
# * which level to display
# * where to send logs
# * how logs should look
# * whether to include timestamps
# * what format to use
# basicConfig() provides a simple way to configure these.

# %(message)s	The actual log message you passed in	>>> "User logged in"
# %(levelname)s	The level name in uppercase	>>> "INFO", "ERROR"
# %(asctime)s	Human-readable timestamp	>>> "2026-09-30 17:35:10,123"
# %(name)s	Name of the logger (often __main__ or module name)	>>> "auth_service"
# %(filename)s	Python source file where the log was triggered	>>> "views.py"
# %(lineno)d	Line number of the log call	>>> 42

logging.basicConfig(level = logging.INFO, format="%(levelname)s: %(message)s")

logging.debug("debugging")
logging.info("information")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# NOTE: basicConfig() is generally used once near the beginning of your program to configure the logging system.

# Log Levels: tell us how important or serious a log message is.
# Python provides five commonly used levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

#DEBUG >>> DEBUG is used for detailed information useful when developing or debugging a program.
# You generally don’t need DEBUG messages during normal operation.
# They’re mainly useful when you’re trying to understand exactly what your program is doing.
import logging
x = 10
logging.basicConfig(level=logging.DEBUG)
logging.debug(f"x has a value of {x} here")


# INFO: represents normal events happening in the program.
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Program started")
logging.info("Loading data")
logging.info("Program ended")


#WARNING: Something unexpected happened, but the program can still continue.
import logging
logging.basicConfig(level=logging.WARNING)
logging.warning("SOMETHING UNEXPECTED HAPPENED")

age = -10
logging.warning(f"Age is negative {age}")


# ERROR: indicates that something went wrong and a particular operation failed.
import logging
try:
    with open("adnan.txt", "r") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    logging.error("File is not there")


# CRITICAL: represents a very serious problem that may prevent the application from continuing correctly.
import logging
logging.critical("Database server is completely unavailable")


# logging level filtering
import logging
logging.basicConfig(level=logging.WARNING)  #>>> this will print warning,error, critical log msgs not the debug and info
logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")

#numeric values of errors
# DEBUG       10
# INFO        20
# WARNING     30
# ERROR       40
# CRITICAL    50


#Logging messages: are created using the appropriate logging method.
import logging
logging.basicConfig(level=logging.INFO) #>>> this will send the log msgs to the terminal

logging.info("This is info")

x = 100
logging.debug(f"x has a value of {x} here")


# Logging to Files
import logging
logging.basicConfig(level=logging.DEBUG, filename="046_logs.log")
# logging.basicConfig(level=logging.DEBUG, filename="logs/046_logs.log") #we can also do this
#it generally has a default mode of append "a" but we can mention "w" write mode so it will over write the old content
# logging.basicConfig(filename="046_logs.log", filemode="w", level=logging.DEBUG)

logging.debug("DEBUGGING")
logging.info("This is logging")


#log formatting
# common format fields:
# %(message)s	The actual log message you passed in	>>> "User logged in"
# %(levelname)s	The level name in uppercase	>>> "INFO", "ERROR"
# %(asctime)s	Human-readable timestamp	>>> "2026-09-30 17:35:10,123"
# %(name)s	Name of the logger (often __main__ or module name)	>>> "auth_service"
# %(filename)s	Python source file where the log was triggered	>>> "views.py"
# %(lineno)d	Line number of the log call	>>> 42

import logging
logging.basicConfig(level=logging.DEBUG, format = "%(levelname)s - %(message)s - %(name)s - %(asctime)s - %(filename)s - %(lineno)d")

#general good format >>> 
# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
# )

try: 
    with open("aaaa.txt","r") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    logging.error("File not found")

#custom timestamp format
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logging.error("Hello")


# Logging Exceptions: This is one of the most useful applications of logging.
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
try:
    with open("thisfile.txt", "r") as file:
        read = file.read()
except FileNotFoundError:
    logging.error("File is not there")

#logging.exception() >>> it doesnt just record the msg or time or lineno etc >>> it records the traceback (A traceback (often called a stack trace) is the step-by-step report showing the sequence of function calls and file lines that led up to an exception.) >>> something like this
# ERROR - An error occurred
# Traceback (most recent call last):
#     ...
# ZeroDivisionError: division by zero
#Primarily use logging.exception() inside except block  >>> It is designed to capture the currently handled exception and its traceback.
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    logging.exception("Zero div error")


