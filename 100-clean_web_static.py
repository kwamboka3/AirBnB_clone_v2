#!/usr/bin/python3
'''Delete module'''
from os import path
import datetime
from fabric.api import local, run, put, env


env.hosts = ['3.236.44.4', '3.235.147.115']


def do_clean(number=0):
    '''Delete files'''

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
