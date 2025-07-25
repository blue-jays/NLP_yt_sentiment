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

logger = logging.getLogger("NLP_logger")