import os
import yaml 
from src.NLP_yt_proj import NLog
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError

class Common():
    def __init__(self):
        pass
    def read_yaml(path_to_yaml:Path) -> ConfigBox:
        """ opens the yaml file
        
        - open the file, load the file, log it as opened.
        - return to ConfigBox
        """
        try:
            with open(path_to_yaml) as yf:
                content = yaml.safe_load(yf)
                NLog.info(f"The file {yf} is loaded successfully")
                return ConfigBox(content)
        except BoxValueError :
            raise ValueError("The yaml file is not found")
        except Exception as e:
            raise e

