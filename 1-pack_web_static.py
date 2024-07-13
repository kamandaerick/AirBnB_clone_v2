#!/usr/bin/python3
'''This script compresses/zips the directory /data/web_static/'''
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    # Create the timestamp string
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Ensure the versions directory exists
    local("mkdir -p versions")

    # Define the full path for the directory to compress
    full_path = "web_static"

    # Create the tarball
    tarball = f"versions/web_static_{timestamp}.tgz"
    result = local(f"tar -czvf {tarball} {full_path}")

    if result.succeeded:
        return tarball
    else:
        return None
