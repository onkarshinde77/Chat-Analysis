from .artifacts_entity import DataPath
import os
import pandas as pd
from contant import CHAT_PATH_DIR_NAME ,CHAT_FILE_NAME

class ChatData:
    def __init__(self):
        self.path = os.path.join(os.getcwd(),CHAT_PATH_DIR_NAME)
        os.makedirs(self.path,exist_ok=True)
        
    def make_file(self,data:pd.DataFrame):
        file_path = os.path.join(self.path,CHAT_FILE_NAME)
        try:
            data.to_csv(file_path, index=False,header=True)
        except Exception as e:
            print(e)
            raise e
        DataPath.chat_data = file_path


        
