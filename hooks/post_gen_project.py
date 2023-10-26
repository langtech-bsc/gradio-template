import os
import shutil
working_directory = os.getcwd();

app_name = "{{cookiecutter.script_name}}.py"
template_selected = "{{cookiecutter.demo_template}}.py"
default_template = "standard.py"

template_dir_path = os.path.join(working_directory, 'templates')
template_list = os.listdir(template_dir_path)

if template_selected in template_list:
    target_file_path = os.path.join(template_dir_path, template_selected)
    new_file_path = os.path.join(template_dir_path, app_name)
    shutil.copy(target_file_path, new_file_path)
    shutil.move(new_file_path,working_directory)
    shutil.rmtree(template_dir_path)
else:
    target_file_path = os.path.join(template_dir_path, default_template)
    new_file_path = os.path.join(template_dir_path, app_name)
    shutil.copy(target_file_path, new_file_path)
    shutil.move(new_file_path,working_directory)
    shutil.rmtree(template_dir_path)