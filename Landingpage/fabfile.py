from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.use_ssh_config = True
env.forward_agent = True
env.user = 'cid3192'
env.hosts = ['hs15.hosting.punkt.de']
env.shell = '/usr/local/bin/bash -l -c'

ext_dir = '/var/apache/cid3192/htdocs/'

@task
def deploy():
	'''
	TEXTClear all caches
	'''
	with cd(ext_dir):
		run("git pull origin master")

