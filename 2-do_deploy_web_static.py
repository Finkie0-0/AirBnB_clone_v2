#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import exists

env.hosts = ['34.224.62.249', '100.25.180.217']


