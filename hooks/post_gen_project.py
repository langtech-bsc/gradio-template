import os
import shutil
import subprocess

working_directory = os.getcwd();

app_name = "{{cookiecutter.script_name}}.py"
template_selected = "{{cookiecutter.demo_template}}.py"
default_template = "standard.py"

templates_dir_path = os.path.join(working_directory, 'templates')
template_selected_path = os.path.join(working_directory, 'templates','{{cookiecutter.demo_template}}' )

template_list = os.listdir(templates_dir_path)

if '{{cookiecutter.demo_template}}' in template_list:
    target_file_path = os.path.join(template_selected_path, template_selected)
    new_file_path = os.path.join(template_selected_path, app_name)
    shutil.copy(target_file_path, new_file_path)
    shutil.move(new_file_path,working_directory)

    requirements_file_path = os.path.join(template_selected_path, 'requirements.txt')
    shutil.move(requirements_file_path, working_directory)

    if '{{cookiecutter.demo_template}}' == 'sagemaker':
        handler_file_path = os.path.join(template_selected_path, 'handler.py')
        shutil.move(handler_file_path, working_directory)
        sagemaker_endpoint_path = os.path.join(template_selected_path, 'sagemaker_endpoint.py')
        shutil.move(sagemaker_endpoint_path, working_directory)
        
else:
    target_file_path = os.path.join(template_selected_path, default_template)

    new_file_path = os.path.join(template_selected_path, app_name)
    shutil.copy(target_file_path, new_file_path)
    shutil.move(new_file_path,working_directory)

    requirements_file_path = os.path.join(template_selected_path, 'requirements.txt')
    shutil.move(requirements_file_path, working_directory)


shutil.rmtree(templates_dir_path)

if'{{cookiecutter.huggin_face_repo_url}}':
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{cookiecutter.huggin_face_repo_url}}'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
