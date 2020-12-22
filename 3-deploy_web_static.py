#!/usr/bin/python3
""" Task 1 """
from datetime import datetime
from fabric.api import local
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['35.231.99.203', '35.196.75.2']


def do_pack():
    """ Task 1 """
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    return filepath


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


def deploy():
    """ Task 3 """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
