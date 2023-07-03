import subprocess
import sys
import os



project_directory = 'C:\\Users\\Vaibhav\\Desktop\\Electrocom\\Marksheet Project\\marksheet'


activate_this_file = os.path.join(project_directory, 'env', 'Scripts', 'activate')
print(activate_this_file)
os.chdir(activate_this_file)
print(os.getcwd())
# exec(compile(open(activate_this_file, "rb").read(), activate_this_file, 'exec'), dict(__file__=activate_this_file))

# subprocess.run('python manage.py runserver', shell=True)