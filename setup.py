import os
import platform

def create_symbolic_link(src, dst):
    if os.path.exists(src):
        if 'com.termux' in os.getenv('PREFIX', ''):
            os.system(f'ln -s $(realpath {src}) $PREFIX/bin/efx')
        elif platform.system() == 'Linux':
            os.system(f'chmod +x {src}')
            os.system(f'ln -s $(realpath {src}) {dst}')
        else:
            print("Unsupported system.")
    else:
        print("Source file does not exist.")

mainFile = 'efx.py'
destination = '/usr/bin/efx'  # Default destination for Linux

create_symbolic_link(mainFile, destination)
