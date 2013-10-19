from fabric.api import put, env, local
from fabric import api
from fabric.contrib.project import rsync_project
import os

env.user = 'adi'
# the servers where the commands are executed
env.hosts = ['197.221.34.5:2224']
project_root = os.path.dirname(__file__)
gen_directory = os.path.join(project_root, "site")
site_root = os.path.join(project_root, "_site")
remote_path = "/var/www/hrh.burgercom.co.za/"
scripts_dir = os.path.join(project_root, "scripts")
generate_script = os.path.join(scripts_dir, "process.py")
map_file = os.path.join(scripts_dir, "map.json")

def deploy():
    local("jekyll build")
    rsync_project(remote_path, site_root, delete=True)

def generate():
    with api.lcd(gen_directory):
        api.local("python %s %s" % (generate_script, map_file))

