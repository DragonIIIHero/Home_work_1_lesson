import os
import shutil

dir_name_root = "my_project"
dir_name_set = "my_project/setting"
dir_name_admin = "my_project/adminapp"
dir_name_auth = "my_project/authapp/templates/authapp"
dir_name_main = "my_project/mainapp/templates/mainapp"
f_init_set = "my_project/setting/__init__.py"
f_init_main = "my_project/mainapp/__init__.py"
f_init_auth = "my_project/authapp/__init__.py"
f_dev = "my_project/setting/dev.py"
f_prod = "my_project/setting/prod.py"
f_model_main = "my_project/mainapp/models.py"
f_model_auth = "my_project/authapp/models.py"
f_views_main = "my_project/mainapp/views.py"
f_views_auth = "my_project/authapp/views.py"
f_base_main = "my_project/mainapp/templates/mainapp/base.html"
f_base_auth = "my_project/authapp/templates/authapp/base.html"
f_index_main = "my_project/mainapp/templates/mainapp/index.html"
f_index_auth = "my_project/authapp/templates/authapp/index.html"

if not os.path.exists(dir_name_root):
     os.makedirs(dir_name_set), os.makedirs(dir_name_admin), os.makedirs(dir_name_auth), os.makedirs(dir_name_main)
else:
    shutil.rmtree(dir_name_root)
    os.makedirs(dir_name_set), os.makedirs(dir_name_admin), os.makedirs(dir_name_auth), os.makedirs(dir_name_main)

f = open(f_init_set, "x"), open(f_init_main, "x"), open(f_init_auth, "x"), open(f_dev, "x"),
open(f_prod, "x"), open(f_model_main, "x"), open(f_model_auth, "x"), open(f_views_main, "x"),
open(f_views_auth, "x"), open(f_base_main, "x"), open(f_base_auth, "x"), open(f_index_main, "x"),
open(f_index_auth, "x")

