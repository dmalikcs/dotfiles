from fabric.api import local, task
from fabric.colors import red, green

@task
def djp_setup(project_name, destination=None):
    '''
    Django project setup with default templates from Django
    '''
    destination = "/home/customer_django_project/projects/%s/" % project_name
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
