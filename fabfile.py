from fabric.api import *
from fabric.contrib.files import exists
import os
from time import strftime

repo = 'https://github.com/NoUseFreak/cicd-test.git'
path = '/var/www/mysite'
env.use_ssh_config = True
env.sudo_user = 'fabric'

env.hosts = ['deploy_ubuntu']
# check read-access to the keys, to be server-independent
keys = ['~/.ssh/id_rsa']
env.key_filename = [key for key in keys if os.access(key, os.R_OK)]

def deploy():
    if not exists(path):
        install()

#    tag_prod()
    update()

# this tags the sha deploy
def tag_prod():
    tag = "prod/%s" % strftime("%Y/%m-%d-%H-%M-%S")
    run('git tag -a %s -m "Prod"' % tag)
    run('git push --tags')

def install():
    run('mkdir -p ' + path)
    with cd(path):
        run('git clone ' + repo + ' .')
        run('curl -s https://getcomposer.org/installer | php')
        run('php composer.phar install --dev')
        run('rm composer.phar')

def update():
    with cd(path):
        run('git remote update')
        run('git pull')
        run('curl -s https://getcomposer.org/installer | php')
        run('php composer.phar install --dev --no-progress')
        run('rm composer.phar')
#        tag = run('git tag -l prod/* | sort | tail -n1')
#        run('git checkout ' + tag)

def deploy():
    if not exists(path):
        install()

#    tag_prod()
    update()

#def rollback(num_revs=1):
#    with cd(path):
#        run('git fetch')
#        tag = run('git tag -l prod/* | sort | tail -n' + str(1 + int(num_revs)) + ' | head -n1')
#        run('git checkout ' + tag)
