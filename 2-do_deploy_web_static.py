#!/usr/bin/python3
""" web server """
from datetime import datetime
from fabric.operations import run, put, sudo
from os.path import exists


env.hosts = ['35.196.67.203', '34.75.15.109']
env.user = 'ubuntu'

def do_deploy(archive_path):
    ''' from archives to servers'''
    if (os.path.exists(archive_path) is False):
        return False
    f = archive_path.split('/')[-1]
    i = '/data/web_static/release/' + \
          "{}".format(f.split('.')[0])
    c = 'data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(i))
        run('sudo tar -xzf {} -C {}/'.format(tmp, i))
        run('sudo rm /tmp/{}'.format(f))
        run('sudo mv {}/web_static {}/'.format(i))
        run('sudo rm -rf {}'.format(c))
        run('sudo ln -s {}/ {}'.format(i, c))
        return True
    except:
        return False
