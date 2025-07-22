'''
Levels (from lowest to highest severity):
DEBUG: Detailed info (for debugging)

INFO: General events (program flow)

WARNING: Something unexpected but still runs

ERROR: Problem occurred

CRITICAL: Serious error; might crash the program
'''

import logging

# logging.basicConfig(level=logging.INFO, 
#                    format='%(asctime)s - %(message)s')
# logging.debug("This is a debug message")
# logging.info("Program started")  
# logging.warningg("This is a warning")
# logging.error("An error occurred")
# logging.critical("Critical issue")                 

# # Logging to a file:
# logging.basicConfig(filename='app.log',
#                     level=logging.DEBUG,
#                     format='%(levelname)s:%(message)s')

# Configure the logger

logging.basicConfig(
    level=logging.DEBUG,  # Show all messages (DEBUG and above)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='example.log',  # Log messages will be saved to this file
    filemode='w'  # 'w' = overwrite each time, use 'a' to append
)

# Sample log messages
logging.debug("This is a DEBUG message (useful for developers)")
logging.info("This is an INFO message (general information)")
logging.warning("This is a WARNING message (something unexpected)")
logging.error("This is an ERROR message (an error occurred)")
logging.critical("This is a CRITICAL message (serious failure)")

print("Logs have been written to example.log")