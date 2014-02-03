from fabric.api import run, local, hosts, cd, task, prefix, lcd
from django.template import Context, Template, loader
#from fabric.contrib import django
#from django.conf import settings
import sys
import os

#sys.path.append(os.path.join(os.environ['PROJECT_HOME'],os.environ['PROJECT_NAME']))
#django.project(os.environ['PROJECT_NAME'])
APP_TEMPLATE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates/')


@task
def create_pkg(app_name):
    files = ['README.rst', 'setup.py', 'MANIFEST.in']
    name = raw_input("Package name:")
    version = raw_input("Version:")
    description = raw_input("description:")
    url = raw_input("Url:")
    author = raw_input("Author:")
    author_email = raw_input("Author email:")
    setup = {
        'name': name,
        'version': version,
        'packages': app_name,
        'description': description,
        'url': url,
        'author': author,
        'author_email': author_email,
        'filename': None,
    }
    local("mkdir %s" % name)
    local("cp -rf %s/* %s" % (APP_TEMPLATE, name))
    with lcd(name):
        for file in files:
            setup['filename'] = file
            local("sed -i -e 's/{{ name }}/%(name)s/g' -e 's/{{ version }}/%(version)s/g' -e 's/{{ packages }}/%(packages)s/g' -e 's/{{ description }}/%(description)s/g' -e 's/{{ url }}/%(url)s/g' -e 's/{{ author }}/%(author)s/g' -e 's/{{ author_email }}/%(author_email)s/g' %(filename)s" % setup)
    local("cp -rf %(packages)s %(name)s" % setup)
    with lcd(name):
        local("python setup.py sdist")
