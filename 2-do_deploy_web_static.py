#!/usr/bin/python3
""" Task 2 """
from datetime import datetime
from fabric.api import put, run, env
from os.path import exists


env.hosts = ['35.231.99.203', '35.196.75.2']


def do_deploy(archive_path=None):
    """ Task 2 """
    if exists(archive_path) is False:
        return False

    name = archive_path.split("/")[-1].split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(name, name))
        run('rm /tmp/{}.tgz'.format(name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(name))
        return True
    except:
        return False
