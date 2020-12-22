#!/usr/bin/python3
""" add date and time"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Task 1 """
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    return filepath
