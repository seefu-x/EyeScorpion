#!/usr/bin/env python3

import os
import shutil

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white


with open('template/sex/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
with open('template/sex/index.html', 'w') as new_index:
    new_index.write(code)