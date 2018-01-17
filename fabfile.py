# -*- coding: utf-8 -*-
# Copyright (C) 2018 boslab.org
# Licensed under the MIT License.
# Created   : 14/Jan/2018 13:12
# @Poject   : boslab
# @AUTHOR   : Francis G. Lee
# Email     : francis@boslab.org



# Definition file for Fabric -- an SSH command-line tool

from fabric.operations import local
from fabric.api import task

@task
def runserver():
    local('python manage.py runserver')

@task
def test():
    local('py.test tests/')

@task
def test_cov():
    local('py.test -s --cov-report term-missing --cov-config tests/.coveragerc --cov app tests/')

@task
def tox():
    local('tox')