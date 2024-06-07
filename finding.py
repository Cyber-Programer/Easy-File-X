import os


def findText(txt, dir=None):
    if not dir:
        dir = os.getcwd()  # Use the current directory if no directory is provided

    if os.path.exists(dir):
        files = os.listdir(dir)
        for file_name in files:
            file_path = os.path.join(dir, file_name)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if txt in content:
                            print('[+] Text Found in File:', file_path)
                except (FileNotFoundError, UnicodeDecodeError):
                    pass
    else:
        print("Directory not found:", dir)
                            

def rmBysz(dir=None):
    
    if not dir:
        dir = os.getcwd()

    if os.path.exists(dir):
        for files in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, files)):
                try:
                    size = os.path.getsize(files) / 1024
                    # print(size)
                    if size <= 0:
                        os.remove(files)
                        print()
                        print(f'[+] File Removed: {files} = {size} kb')
                except FileNotFoundError:
                    pass
