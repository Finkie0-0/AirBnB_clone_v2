#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate the .tgz archive"""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filePath = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions')
    created = local("tar -cvzf {} web_static".format(filePath))

    if created.succeeded:
        return filePath
