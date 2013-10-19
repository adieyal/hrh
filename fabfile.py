from fabric.api import put, env, local
from fabric.contrib.project import rsync_project

env.user = 'adi'
# the servers where the commands are executed
env.hosts = ['197.221.34.5:2224']

def deploy():
    local("jekyll build")
    rsync_project("/var/www/hrh.burgercom.co.za/", "site/_site/", delete=True)

