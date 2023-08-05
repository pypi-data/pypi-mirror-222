import os
import platform
import argparse
import PyInstaller.__main__ as build

from rfidtools.core import gui_loop


parser = argparse.ArgumentParser(
    prog='rfidtools',
    description='Tool for RFID tag production at CIOT.',
    epilog='Use "python -m rfidtools" to run from the command line.')

parser.add_argument('-b', '--build-exe',
                    required=False,
                    action='store_true',
                    help='Build the program into an exe to be placed on the desktop')

BUILD = vars(parser.parse_args())['build_exe']


if not BUILD:
    gui_loop()

else:
    if platform.system() == 'Windows':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        build.run([
            f'{dir_path}\\__main__.py',
            f'--distpath {desktop}',
            '-F',
            '-n RFID_Tools',
            '--windowed',
            '-i RFID_Icon.ico'])
    else:
        print('Building to .exe is only supported on Windows.')
        raise SystemError
