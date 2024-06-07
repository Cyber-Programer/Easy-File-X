
import random
import string
import shutil
import os

nameList = []
folderNameList = []

def makeName(amount,fileName) :
    for i in range(int(amount)):
        
        if int(amount) > 104:
            print('[x] Max limit 104')
            break
        
        elif i >= 52:
            if i >= 104:
                
                name = ''.join(random.choices(string.ascii_letters, k=3))
                
                if name not in nameList:
                    nameList.append(name+fileName)    
                
            name = ''.join(random.choices(string.ascii_letters, k=2))
            
            if name not in nameList:
                nameList.append(name+fileName)
            
        name = random.choice(string.ascii_letters,)
            
        if name not in nameList:
            nameList.append(name+fileName)

    return nameList


def makeFile(dir,data):
    
    amount , fileName = data.split(',')
    
    
    if dir:
        if os.path.exists(dir):
            
            fileNameList = makeName(amount=amount,fileName=fileName)
            
            for file in fileNameList:
                try:
                    with open(file,'w') as f:
                        f.write('')
                        f.close()
                except Exception as e:
                    print(e)
                
        else:
            print(f'[x] Path : {dir} Not Exist')
    else:
        
        amount , fileName = data.split(',')
        
        fileNameList = makeName(amount=amount,fileName=fileName)
        
        for file in fileNameList:
            
            try:
                with open(file,'w') as f:
                    f.write('')
                    f.close()
            except Exception as e:
                print(e)



def makeFolderName(amount) :
    for i in range(int(amount)):
        
        if int(amount) > 104:
            print('[x] Max limit 104')
            break
        
        elif i >= 52:
            if i >= 104:
                
                name = ''.join(random.choices(string.ascii_letters, k=3))
                    
                if name not in folderNameList:
                    folderNameList.append(name)    
                
            name = ''.join(random.choices(string.ascii_letters, k=2))
            
            if name not in folderNameList:
                folderNameList.append(name)
            
        name = random.choice(string.ascii_letters,)
            
        if name not in folderNameList:
            folderNameList.append(name)

    return folderNameList



def makeFolder(dir,amount):
    
    
    if dir:
        if os.path.exists(dir):
            folderName = makeFolderName(amount)
            for folder in folderName:
                os.mkdir(folder)
        else:
            print(f'[x] Path : {dir} Not Exist')
            
            

    else:
        folderName = makeFolderName(amount)
        for folder in folderName:
            os.mkdir(folder)

def makeCustomFile(file,dir):
    if dir:
        if os.path.exists(dir):
            if os.path.exists(file):
                
                with open(file,'r') as f:
                    data = f.read().split('\n')
                    
                    for filename in data:
                        if filename != '':
                            filePath = os.path.join(dir,filename)
                            with open(filePath,'w') as write:
                                write.write('')
            else:
                print(f'[x] File : {file} Not Exist')
        else:
            print(f'[x] Dir : {dir} Not Exist')

            
        
    else:
        if os.path.exists(file):
            
            with open(file,'r') as f:
                data = f.read().split('\n')
                
                for filename in data:
                    if filename != '':
                        with open(filename,'w') as write:
                            write.write('')
        else:
            print(f'[x] File : {file} Not Exist')


def makeCustomFolder(file,dir):
    if dir:
        if os.path.exists(dir):
            if os.path.exists(file):
                
                with open(file,'r') as f:
                    data = f.read().split('\n')
                    for folder in data:
                        if folder != '':
                            os.mkdir(folder)
            else:
                print(f'[x] File : {file} Not Exist')
                

        else:
            print(f'[x] Dir : {dir} Not Exist')
    
    
    else:
        
        if os.path.exists(file):
                
                with open(file,'r') as f:
                    data = f.read().split('\n')
                    for folder in data:
                        if folder != '':
                            os.mkdir(folder)

        else:
            print(f'[x] File : {file} Not Exist')



def coppyFiletoFolder(file,dir):
    if dir:
        if os.path.exists(dir):
            if os.path.exists(file):
                ls = os.listdir(dir)
                for data in ls:
                    if os.path.isdir(os.path.join(dir,data)):
                        if ',' in file:
                            filelist = file.split(',')
                            
                            for mainFile in filelist:
                                if mainFile !='':
                                    shutil.copy(mainFile,os.path.join(dir,data))
                            
                        else:
                            shutil.copy(file,os.path.join(dir,data))

                
            else:
                print(f'[x] File : {file} Not Exist')
    
        else:
            print(f'[x] Dir : {dir} Not Exist')
        
    
    else:
        # dir = os.getcwd()
        
        if os.path.exists(file):
                ls = os.listdir()
                for data in ls:
                    if os.path.isdir(data):
                        if ',' in file:
                            filelist = file.split(',')
                            
                            for mainFile in filelist:
                                if mainFile !='':
                                    shutil.copy(mainFile,data)
                            
                        else:
                            shutil.copy(file,data)
        else:
            print(f'[x] File : {file} Not Exist')
        
    