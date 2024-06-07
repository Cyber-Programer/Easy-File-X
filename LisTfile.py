import os

Cdir = os.getcwd()

def allListFile(dir):
    files = []
    
    if dir:
        if os.path.exists(dir):
            for root,_,fileNames in os.walk(dir):
                for filename in fileNames:
                        files.append(filename)
        else:
            print('[-] Fiel Path not Exist')
        
        
    else:
        dir = Cdir
        if os.path.exists(dir):
            for root,_,fileNames in os.walk(dir):
                for filename in fileNames:
                        files.append(filename)  # Corrected concatenation
    return files


def listFile(dir):
    files = []
    
    if dir:
        if os.path.exists(dir):
            for fileNames in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, fileNames)):
                    files.append(fileNames)
                # for filename in fileNames:
                #         files += filename + ' '
        else:
            print('[-] Fiel Path not Exist')
        
        
    else:
        dir = Cdir
        if os.path.exists(dir):
            for fileNames in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, fileNames)):
                    files.append(fileNames)
    return files



def countFile(dir):
    files = []
    if dir:
        for filename in os.listdir(dir):
            if os.path.isfile(os.path.join(dir,filename)):
                files.append(filename)
    else:
        dir = Cdir
        for filename in os.listdir(dir):
            if os.path.isfile(os.path.join(dir,filename)):
                files.append(filename)
    return len(files)
    

def allCountFile(dir):
    files = []
    
    if dir:
        if os.path.exists(dir):
            for root,_,fileNames in os.walk(dir):
                for filename in fileNames:
                        files.append(filename)
            return len(files)
        else:
            print('[-] Fiel Path not Exist')
        
        
    else:
        dir = Cdir
        if os.path.exists(dir):
            for root,_,fileNames in os.walk(dir):
                for filename in fileNames:
                        files.append(filename)  # Corrected concatenation
            
            return len(files)
            
    return files



def listFolder(dir):
    files = []
    
    if dir:
        if os.path.exists(dir):
            for folderNames in os.listdir(dir):
                if os.path.isdir(os.path.join(dir, folderNames)):
                    files.append(folderNames)
                # for filename in folderNames:
                #         files += filename + ' '
        else:
            print('[-] Fiel Path not Exist')
        
        
    else:
        dir = Cdir
        if os.path.exists(dir):
            for folderNames in os.listdir(dir):
                if os.path.isdir(os.path.join(dir, folderNames)):
                    files.append(folderNames)
    return files


def countFolder(dir):
    files = [] 
    
    if dir:
        if os.path.exists(dir):
            for folderNames in os.listdir(dir):
                if os.path.isdir(os.path.join(dir, folderNames)):
                    files.append(folderNames)
                # for filename in folderNames:
                #         files += filename + ' '
        else:
            print('[-] Fiel Path not Exist')
        
        
    else:
        dir = Cdir
        if os.path.exists(dir):
            for folderNames in os.listdir(dir):
                if os.path.isdir(os.path.join(dir, folderNames)):
                    files.append(folderNames)
    return len(files)


def listFileExtension(extension,dir):
    
    if dir:
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, file)):
                    if file.endswith(extension):
                        print(file)
        else:
            print('[-] Directory Path does not exist')

    
    else:
        dir = Cdir
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, file)):
                    if file.endswith(extension):
                        print(file)
        else:
            print('[-] Directory Path does not exist')
    

def listFileBySize(dir):
    
    if dir:
        if os.path.exists(dir):
            for file in os.listdir(dir):                
                print(file,'|', f"{os.path.getsize(file) / 1024:.2f} KB")

        else:
            print('[-] Directory Path does not exist')
    else:
        dir = Cdir
        if os.path.exists(dir):
            for file in os.listdir(dir):
                print(file, '|',f"{os.path.getsize(file) / 1024:.2f} KB")
        else:
            print('[-] Directory Path does not exist')
            