#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: logs

short_description: copy logs 

version_added: "1.0"

description: copy logs to chosen destination and name it with current datetime

author:
    - Your Name (sulim.obei@gmail.com)
'''

EXAMPLES = r'''
tasks
  - logs:

'''

from ansible.module_utils.basic import AnsibleModule



import datetime
import shutil
import os

original = r'/var/log/syslog'
target = r'/home/'  + datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S") + '.txt'

shutil.copyfile(original, target)
