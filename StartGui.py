import platform
import os
import sys
from shutil import which
from subprocess import call


if sys.version_info[:2] < (3, 7):
    print("Requires Python 3.7 or newer. "
          "Python %d.%d detected" % sys.version_info[:2])
    sys.exit(-1)

if platform.system() == 'Windows':
    OS = 'Windows'
elif platform.system() == 'Linux':
    OS = 'Linux'
elif platform.system() == 'Darwin':
    OS = 'Darwin'
path = os.getcwd()
if OS == 'Windows':
    cache = path + '\Core\Cache'
elif OS == 'Darwin':
    cache = path + '/Core/Cache'
else:  # Linux
    cache = path + '/Core/Cache'

isExist = os.path.exists(cache)
if not isExist:  # Create a new directory because it does not exist
    os.system('pip install -r requirements.txt')
    os.system('pip install latex')
    if OS == 'Windows':
        if which('latex'):
            print('latex installed')
        else:
            print('Please install Latex before using the software')
            sys.exit(-1)
    elif OS == 'Darwin':
        if which('latex'):
            print('latex installed')
        else:
            os.system(
                '/bin / bash - c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
            os.system('brew install mactex')
    else:  # Linux
        pwd = 'password'
        cmd = 'sudo apt install -y idle3 texlive-latex-extra cm-super dvipng'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)

        # os.system('sudo apt install idle3')
    os.makedirs(cache)


if OS == 'Windows':
    import Core.Windows_GUI
elif OS == 'Darwin':
    import Core.Mac_GUI
else:  # Linux
    import Core.Windows_GUI
