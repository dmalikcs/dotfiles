# .bashrc

#####user specfic aliases 
alias gl='cd /home/krunk1/goriladesigns/'
alias dj='cd /home/krunk1/djangodevelopers'
alias ks='cd /home/dmalik5/krunksystems'
alias dm='cd /home/dmalik5/'
alias fb='cd /home/customer_django_project/giftwrapcompany.com/'
alias latest='cd /download/blender/latest/'
alias r='python manage.py runserver 192.168.1.101:8002'


# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME='/home/customer_django_project/projects'
source /usr/local/bin/virtualenvwrapper.sh


#### Fusionbox Project setting ###
export FB='/home/customer_django_project/giftwrapcompany.com/'
