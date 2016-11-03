#!/usr/bin/env python
"""
This script is used to run tests, create a coverage report and output the
statistics at the end of the tox run.
To run this script just execute ``tox``
"""
import re

from fabric.api import local, warn
from fabric.colors import green, red

if __name__ == '__main__':
    local('pip install -r test_requirements.txt')
    local('flake8 --ignore=E126 --ignore=W391 --ignore=E501 --statistics'
          ' --exclude=submodules,migrations,build,.tox,.git,runtests.py,venv')
    local('coverage run --source="webapp" webapp/manage.py test -v 2')
    local('coverage html -d coverage --omit="*__init__*,*/settings/*,'
          '*/migrations/*,*/tests/*,*admin*"')
    total_line = local('grep -n pc_cov coverage/index.html', capture=True)
    percentage = float(re.findall(r'(\d+)%', total_line)[-1])
    if percentage < 100:
        warn(red('Coverage is {0}%'.format(percentage)))
    print(green('Coverage is {0}%'.format(percentage)))
