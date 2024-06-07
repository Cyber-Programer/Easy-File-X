import os
import platform

def create_symbolic_link(src, dst):
    if os.path.exists(src):
        if platform.system() == 'Linux':
            os.system(f'chmod +x {src}')
            os.system(f'ln -s $(realpath {src}) {dst}')
        elif 'com.termux' in os.getenv('PREFIX', ''):
            os.system(f'ln -s $(realpath {src}) $PREFIX/bin/efx')

mianFile = 'efx.py'

create_symbolic_link(mianFile, '/usr/bin/efx')
