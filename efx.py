#!/usr/bin/env python

'''

                           EasyFileX Tool
            
                 Author: Cyber-Programmer (@root_lovs)

            This tool may solve your file management problems

'''

import argparse
from LisTfile import *
from rmv import *
from finding import *
from copyPest import *
import os
import sys

def main():
    example = '''
Example usage:
    efx -l                     # List files
    efx -lF                    # List files from folders
    efx -lfx .txt              # List files with the specified extension (.txt)
    efx -al                    # List all files and folders
    efx -cf                    # Count files
    efx -cF                    # Count folders
    efx -cfF                   # Count all files and folders
    efx -cfaF                  # Copy file in all folder
    efx -mf 20,.txt            # Make random file
    efx -mF 20                 # Make random folder
    efx -mcf file.txt          # Make custom File
    efx -mcF folder.txt        # Make custom Folder
    efx -fsize                 # List files with sizes
    efx -ft "search text"      # Find text in existing files
    efx -rx .log               # Remove files with the specified extension (.log)
    efx -rmef                  # Remove empty files from folders
    efx -rmeF                  # Remove emty folder from dir
    efx -d /path/to/dir        # Specify the directory path
    '''

    parser = argparse.ArgumentParser(
        prog='efx',
        description='EasyFileX tool may solve your file management problems.',
        epilog='''
Thank you for using EasyFileX!
Happy managing!

- Cyber-Programmer (@root_lovs)
''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-l', '--list', action="store_true", help="Display a list of files")
    parser.add_argument('-lF', '--listfFromF', action="store_true", help="Display a list of files from folders")
    parser.add_argument('-lfx', '--lstfilex', metavar='', action="store", help="List files with the specified extension")
    parser.add_argument('-al', '--allList', action="store_true", help="Display a list of all files and folders")
    parser.add_argument('-cf', '--countFiles', action="store_true", help="Count the number of files")
    parser.add_argument('-cF', '--countFolders', action="store_true", help="Count the number of folders")
    parser.add_argument('-cfF', '--countff', action="store_true", help="Count all files and folders")
    parser.add_argument('-cfaF', '--copyfallF', action="store", help="coppy file/files in all folder")
    parser.add_argument('-mf','--makeFile', action='store', help='Make random file')
    parser.add_argument('-mF','--makeFolder', action='store', help='Make random folder')
    parser.add_argument('-mcf','--mkcfile',action='store',help='Make custom file')
    parser.add_argument('-mcF','--mkcFolder',action='store',help='Make custom folder')
    parser.add_argument('-fsize', '--listFileBysize', action="store_true", help="List files along with their sizes")
    parser.add_argument('-ft', '--findTxt', metavar='', action="store", help="Search for text in existing files")
    parser.add_argument('-rx', '--rmx', metavar='', action="store", help="Remove files with the specified extension")
    parser.add_argument('-rmef', '--rmemtyf', action="store_true", help="Remove empty files from folders")
    parser.add_argument('-rmeF', '--rmemtyF', action="store_true", help="Remove empty folder from dir")
    parser.add_argument('-d', '--dir', action="store", metavar='', help="Specify the directory path")

    # Parse the arguments
    args = parser.parse_args()

    # If no arguments are provided, print the example usage
    if len(sys.argv) == 1:
        print(example)
        sys.exit(0)

    if args.list:
        if args.dir:
            files = listFile(dir=args.dir)
            for file in files:
                print(file)
        else:
            files = listFile(dir=False)
            for file in files:
                print(file)
    
    elif args.allList:
        if args.dir:
            allFiles = allListFile(dir=args.dir)
            for file in allFiles:
                print(file)
        else:
            allFiles = allListFile(dir=False)
            for file in allFiles:
                print(file)
    
    elif args.countFiles:
        if args.dir:
            amount = countFile(dir=args.dir)
            print()
            print('[+] Total File Found: ', amount)
        else:
            amount = countFile(dir=False)
            print()
            print('[+] Total File Found: ', amount)
    
    elif args.countff:
        if args.dir:
            amount = allCountFile(dir=args.dir)
            print()
            print('[+] Total All File/Folder Found: ', amount)
        else:
            amount = allCountFile(dir=False)
            print()
            print('[+] Total All File/Folder Found: ', amount)
    
    elif args.listfFromF:
        if args.dir:
            allFolder = listFolder(args.dir)
            for folder in allFolder:
                print(folder)
        else:
            allFolder = listFolder(dir=False)
            for folder in allFolder:
                print(folder)
    
    elif args.countFolders:
        if args.dir:
            amount = countFolder(dir=args.dir)
            print('[+] Total Folder Found: ', amount)
        else:
            amount = countFolder(dir=False)
            print('[+] Total Folder Found: ', amount)
                
    elif args.rmx:
        if args.dir:
            removeFile(dir=args.dir, extension=args.rmx)
        else:
            removeFile(dir=False, extension=args.rmx)
    
    elif args.lstfilex:
        if args.dir:
            listFileExtension(extension=args.lstfilex, dir=args.dir)
        else:
            listFileExtension(extension=args.lstfilex, dir=False)
            
    elif args.findTxt:
        if args.dir:
            findText(txt=args.findTxt, dir=args.dir)
        else:
            findText(txt=args.findTxt, dir=False)
    
    elif args.rmemtyf:
        if args.dir:
            rmBysz(dir=args.dir)
        else:
            rmBysz(dir=False)
    
    elif args.listFileBysize:
        if args.dir:
            listFileBySize(dir=args.dir)
        else:
            listFileBySize(dir=False)
        
    elif args.makeFile:
        if args.dir:
            makeFile(dir=args.dir,data=args.makeFile)
        else:
            makeFile(dir=False,data=args.makeFile)
    
    elif args.makeFolder:
        if args.dir:
            makeFolder(dir=args.dir,amount=args.makeFolder)
        else:
            makeFolder(dir=False,amount=args.makeFolder)
    
    elif args.rmemtyF:
        if args.dir:
            remove_emty_folder(dir)
        else:
            remove_emty_folder(dir=False)
    
    elif args.mkcfile:
        if args.dir:
            makeCustomFile(file=args.mkcfile,dir=args.dir)
        else:
            makeCustomFile(file=args.mkcfile,dir=False)
    
    elif args.mkcFolder:
        if args.dir:
            makeCustomFolder(file=args.mkcFolder,dir=args.dir)
        else:
            makeCustomFolder(file=args.mkcFolder,dir=False)
    
    elif args.copyfallF:
        if args.dir:
            coppyFiletoFolder(file=args.copyfallF,dir=args.dir)
        else:
            coppyFiletoFolder(file=args.copyfallF,dir=False)
            

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
