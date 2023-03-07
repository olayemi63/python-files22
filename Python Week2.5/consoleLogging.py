# LOGGING

# Keeping track\ of our code as it runs
#Errors, further info for Developers to note.

import logging 

# a way to track and capture what's going on with our program/code

"""
"CRITICAL"            LEVEL 5 [Highest]
"Error"               LEVEL 4
"Warning"             LEVEL 3
"Info"                LEVEL 2
"Debug"               LEVEL 1 [Lowest]

"""


# ERROR HANDLING

# Configure the logging module


logging.basicConfig(
        level = logging.DEBUG, 
        filename = "errors.log", 
        format = "%(levelname)s : %(asctime)s - %(message)s"
        
)

# logging.debug("This is a debugging level message.")

logging.critical("THIS IS A CRITICAL LEVEL message!!!!!")
logging.error("This is an Error message!!!!!")
logging.warning("This is a warning Level Message.")
logging.info("This is an Informational Level Message.")
logging.debug("This is a debugging level message.")

# Print isn't always viable for debugging
# Print is mainly for the user
# print("This is a debug message.")