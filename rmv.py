import os

Cdir = os.getcwd()

def removeFile(extension, dir):
    if dir:
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, file)):
                    if file.endswith(extension):
                        file_path = os.path.join(dir, file)
                        try:
                            os.remove(file_path)
                            print(f"File '{file_path}' with extension '{extension}' successfully removed.")
                        except OSError as e:
                            print(f"Error: {file_path} : {e.strerror}")
        else:
            print('[-] Directory Path does not exist')

    
    else:
        dir = Cdir
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, file)):
                    if file.endswith(extension):
                        file_path = os.path.join(dir, file)
                        try:
                            os.remove(file_path)
                            print(f"File '{file_path}' with extension '{extension}' successfully removed.")
                        except OSError as e:
                            print(f"Error: {file_path} : {e.strerror}")
        else:
            print('[-] Directory Path does not exist')



def remove_emty_folder(dir):
    
    if dir:
        
        for item in os.listdir(dir):
            item_path = os.path.join(dir, item)  # Get the full path to the item
            if os.path.isdir(item_path):
                size_kb = os.path.getsize(item_path) / 1024
                if size_kb == 0:
                    os.rmdir(item_path)
    else:
        dir = Cdir
        for item in os.listdir(dir):
            item_path = os.path.join(dir, item)  # Get the full path to the item
            if os.path.isdir(item_path):
                size_kb = os.path.getsize(item_path) / 1024
                if size_kb == 0:
                    os.rmdir(item_path)


