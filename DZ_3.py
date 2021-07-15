import os
import shutil

dir_name_temp = "my_project/templates"
dir_name_main = "my_project/templates/mainapp"
dir_name_aut = "my_project/templates/authapp"

if not os.path.exists(dir_name_temp):
    shutil.copytree("my_project/mainapp/templates/mainapp", dir_name_main)
    shutil.copytree("my_project/authapp/templates/authapp", dir_name_aut)
else:
    shutil.rmtree(dir_name_temp)
    shutil.copytree("my_project/mainapp/templates/mainapp", dir_name_main)
    shutil.copytree("my_project/authapp/templates/authapp", dir_name_aut)