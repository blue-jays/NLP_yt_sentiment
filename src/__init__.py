import os
import sys 
import logging 

# customize the output 
logging_out = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


Log_dir = "Logs"
log_filepath = os.path.join(Log_dir, "logger.log")#join the directoty with the file created
os.makedirs(Log_dir, exist_ok = True) # If already there, skip


# customize the logging. 
logging.basicConfig(  
		level = logging.INFO,  # logging depth - 1
		format = logging_out,
        
        handlers=[
            logging.FileHandler(log_filepath), # sends log to the file
            logging.StreamHandler(sys.stdout)  # sends to the terminal
        ]      
)

NLog = logging.getLogger("NLP_logger")
# creating a logger, named (NLP_logger), that will appear on the logs.
# NLog is just the object we use to call the logger.


### what are we doing here
"""
Here we are making a custom logger, that is in the src init file. 
So that we can import it anywhere.

"""