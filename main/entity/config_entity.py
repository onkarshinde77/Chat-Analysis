from .artifacts_entity import DataPath
import os
import pandas as pd
from constant import CHAT_PATH_DIR_NAME ,CHAT_FILE_NAME

class ChatData:
    def __init__(self):
        self.path = os.path.join(os.getcwd(),CHAT_PATH_DIR_NAME)
        os.makedirs(self.path,exist_ok=True)
        
    def make_file(self,data:pd.DataFrame):
        file_path = os.path.join(self.path,CHAT_FILE_NAME)
        try:
            data.to_csv(file_path, index=False,header=True)
            DataPath.chat_data_path = file_path
        except Exception as e:
            print(e)
            raise e
    def get_path(file_name : str)->str:
        dir = os.getcwd()
        return dir