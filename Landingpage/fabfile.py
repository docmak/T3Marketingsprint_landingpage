from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.use_ssh_config = True
env.forward_agent = True
env.user = 'cid3052'
env.hosts = ['hs14.hosting.punkt.de']
env.shell = '/usr/local/bin/bash -l -c'

ext_dir = '/var/apache/cid3052/htdocs/typo3conf/ext/'

@task
def deploy():
	'''
	TEXTClear all caches
	'''
	with cd(ext_dir):
		run("cd ejw_templates && git pull origin master && cd ../ejw_calendar && git pull origin master && cd ../ejwintern && git pull origin master")
#        run("cd ../ejw_calendar && git pull origin master")
#        run("cd ../ejwintern && git pull origin master")
