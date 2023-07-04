import platform
import os
from Core import Mac_GUI, Window_GUI


if platform.system() == 'Windows':
    OS = 'Windows'
if platform.system() == 'Linux':
    OS = 'Linux'
elif platform.system() == 'Darwin':
    OS = 'Darwin'

os.system('pip install -r requirements.txt')

if OS == 'Windows':
    Window_GUI.run()
elif OS == 'Darwin':
    Mac_GUI.run()
else:  # Linux
    Window_GUI.run()