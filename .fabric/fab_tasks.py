from fabric.api import local, task, hosts, cd, run, prefix, lcd
from fabric.colors import red, green
from fabric.api import env
from utils import djangotasks
import os

#with open('.env') as f:
#    env.password = f.readline().strip()
env.password = ""

# To-do
#   Add the deployment setting with django project
#   static/media files management
# backup planning for fabric script


REMOTE_PROJECT = {
    'deepakmalik': {
        'server': '',   # Deployment server
        'port': '',     # Deployment ssh port number
        'ssh_user': '',  # ssh user name
        'project_path': '/home/openerpi/public_html/deepakmalik.in/',
        'django_project_path': '/home/openerpi/public_html/deepakmalik.in/deepakmalik/',
        'domain': 'deepakmalik.in',
        'env': '/home/openerpi/.virtualenv/',
        'git': 'git@bitbucket.org:dmalikcs/deepakmalik.in.git',
        'branch': 'vps',
        'requirement': 'requirements.txt'
    },
    'openerp': {
        'server': '',   # Deployment server
        'port': '',     # Deployment ssh port number
        'ssh_user': '',  # ssh user name
        'project_path': '/home/openerpi/public_html/openerp.in/',
        'django_project_path': '/home/openerpi/public_html/openerp.in/openerp/',
        'domain': 'openerp.in',
        'env': '/home/openerpi/.virtualenv/',
        'git': 'git@bitbucket.org:dmalikcs/openerp.git',
        'branch': 'live',
        'requirement': 'requirements.txt'
    },
    'krunksystems': {
        'server': '',   # Deployment server
        'port': '',     # Deployment ssh port number
        'ssh_user': '',  # ssh user name
        'project_path': '/home/openerpi/public_html/krunksystems.com/',
        'django_project_path': '/home/openerpi/public_html/krunksystems.com/krunksystems/',
        'domain': 'krunksystems.com',
        'env': '/home/openerpi/.virtualenv/',
        'git': 'git@bitbucket.org:dmalikcs/krunksystems.git',
        'branch': 'live',
        'requirement': 'requirements.txt'
    },
    'powerbazaar': {
        'server': '',   # Deployment server
        'port': '',     # Deployment ssh port number
        'ssh_user': '',  # ssh user name
        'project_path': '/home/openerpi/public_html/powerbazaar.in/',
        'django_project_path': '/home/openerpi/public_html/powerbazaar.in/powerbazaar/',
        'domain': 'powerbazaar.in',
        'env': '/home/openerpi/.virtualenv/',
        'git': 'git@bitbucket.org:dmalikcs/powerbazaar.git',
        'branch': 'master',
        'requirement': 'requirements.txt'
    },
}


@task
def djp_setup(project_name, destination=None):
    '''
    djp_setup: Django project setup

    syntax:
        fab djp_setup:project_name=""
    '''
    HOME = os.environ['HOME']
    destination = "%s/projects/%s/" % (HOME, project_name)
    template = 'https://github.com/dmalikcs/django-project-template/archive/master.zip'
    #local("mkdir %s" % destination)
    local("django-admin.py startproject --template=%s  %s %s" % (template, project_name, destination))
    print("Project created" + green("successfully"))
    local("git init %s" % destination)


@task
def installapp(app_name=None, app_type=None):
    '''
    fab installapp:app_name='Apps name',app_type=''
    app_type = tastypie/celery
    '''
    if app_type == 'tastypie':
        template = 'https://github.com/dmalikcs/django-tastypie-app-template/archive/master.zip'
    elif app_type == 'celery':
        template = 'https://github.com/dmalikcs/django-celery-app-template/archive/master.zip'
    else:
        template = 'https://github.com/dmalikcs/django-app-template/archive/master.zip'
    local("python manage.py startapp --template=%s %s" % (template, app_name, ))


@task
@hosts('openerpi@199.195.119.66:7822')
def update():
    project_name = os.environ['PROJECT_NAME']
    project = REMOTE_PROJECT.get(project_name)
    with prefix("source %s/%s/bin/activate" % (project.get('env'), project_name)), cd(project.get('django_project_path')):
        run("git pull origin %s" % project.get('branch'))
        run("python manage.py syncdb --migrate")
        run("touch ./tmp/restart.txt")


@task
@hosts('openerpi@199.195.119.66:7822')
def deploy(project_name):
    project = REMOTE_PROJECT.get(project_name)
    with cd(project.get('env')):
        run("virtualenv -p /usr/bin/python2.6 %s" % project_name)
    # validate Project path exists & clone git ptoject
    with cd(project.get('project_path')):
        run("git clone -b %s %s" % (project.get('branch'), project.get('git')))
    # syncdb &  migration
    with prefix("source %s/%s/bin/activate" % (project.get('env'), project_name)), cd(project.get('django_project_path')):
        run("pip install -r %s" % project.get('requirement'))
        run("python manage.py syncdb")
        run("python manage.py migrate")
        run("fab setup")


@task
@hosts('openerpi@199.195.119.66:7822')
def install_requirment(project_name):
    project = REMOTE_PROJECT.get(project_name)
    with prefix("source %s/%s/bin/activate" % (project.get('env'), project_name)), cd(project.get('django_project_path')):
        run("pip install -r %s" % project.get('requirement'))
        run("python manage.py syncdb --migrate")
