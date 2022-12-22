#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates .tgz archive from the /web_static's content
    """
    local('mkdir -p versions')
    created = local("tar -czvf versions/web_static_{}.tgz web_static/".format((
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))), capture=True)

    if created.succeeded:
        return created
    return None
