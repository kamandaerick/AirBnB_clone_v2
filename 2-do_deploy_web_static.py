#!/usr/bin/python3
"""Deploy web static"""
from fabric.api import *
from datetime import datetime
from os import path, expanduser

env.hosts = ['3.94.213.52', '54.175.144.43']
env.user = 'ubuntu'
env.key_filename = expanduser('~/.ssh/id_rsa')


def do_deploy(archive_path):
    """Deploy web files to server"""
    try:
        if not path.exists(archive_path):
            print(f"Archive path {archive_path} does not exist.")
            return False

        # Upload archive
        put(archive_path, '/tmp/')

        # Create target directory
        timestamp = archive_path[-18:-4]
        target_dir = f"/data/web_static/releases/web_static_{timestamp}/"
        run(f'sudo mkdir -p {target_dir}')

        # Uncompress archive and delete .tgz
        run(f'sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C {target_dir}')

        # Remove archive
        run(f'sudo rm /tmp/web_static_{timestamp}.tgz')

        # Move contents into host web_static
        run(f'sudo mv {target_dir}web_static/* {target_dir}')

        # Remove extraneous web_static dir
        run(f'sudo rm -rf {target_dir}web_static')

        # Delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Re-establish symbolic link
        run(f'sudo ln -s {target_dir} /data/web_static/current')

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    # Return True on success
    return True
