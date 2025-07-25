""" This is the automated script that is used to make the project structure for this project.
"""

import os 
from pathlib import Path
import logging


## log to a file 

# log_file = os.path.join("project.log", "Logs") # where and which file

# logging.basicConfig(
#     filename = "Logs/project.log",  # this is where the file is.
#     filemode= "a",
#     level = logging.INFO,
#     format='[%(asctime)s] %(levelname)s: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )


project_name = "NLP_yt_proj"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # 
    
    f"src/{project_name}/components/__init__.py", # ingestion
    
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    f"src/{project_name}/pipeline/__init__.py",
    
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    
    f"src/{project_name}/constants/__init__.py",
    
    
    f"config/config.yaml",
    f"params.yaml",
    f"main.py",
    f"Docker.py",
    f"setup.py",
    f"research/research.ipynb",
    f"templates/index.html",
    f"Logs/project.log"
    
]



# automating the creation of files 
for filepath in list_of_files:
    filepath = Path(filepath)   # strings_path to object path.
    filedir, filename = os.path.split(filepath)  # get the filename(last one), get the directory this file should be in 
    
    if filedir !="":
        os.makedirs(filedir, exist_ok = True) #function to make the file, if it exist, then skip, exist_ok
        logging.info(f"Creating directory at {filedir}, for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # if the file does not exist or the file is empty.
        with open(filepath, "w") as file:
            pass
            logging.info(f"Creating empty file: ")
            
    else:
        logging.info(f"{filename} already exists")        