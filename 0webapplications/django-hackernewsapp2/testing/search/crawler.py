import os 
import tkinter as tk 
# some comments 
#
#
#
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
#def create_data_files(project_name):
    
create_project_dir('thenewboston')