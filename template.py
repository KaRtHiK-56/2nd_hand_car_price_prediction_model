#this template.py file is used to automate the creation of a folder structure file paths 
import os
from pathlib import Path

project_name = "2nd_hand_car_price"

list_of_files = [

    f"{project_name}/__init__.py",
    #components subfolder
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    #logging and exception
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    #pipeline subfolder
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",


]

#for creating the folder and subfolder structure 
for filepath in list_of_files:
    #identifying the machine folder(windows/macos/ubuntu)
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #if not empty create folder and files
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    #if it is not empty , new file or newly written code is appended
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    #finally if the folder is already there print the message
    else:
        print(f"file is already present at: {filepath}")


#USE python tempate.py to create the folder structure

