import os
import pathlib


def createTestData(dir, fileEnding):
    """creates 10 files with specified file ending in the local "files" directory """
    numbers = range(0,10)
    for count in numbers:
        filename = '{dir}myNewFile{identifier}.{ending}'.format(identifier = count, ending = fileEnding, dir = dir)
        f = open(filename, "w") 


def getAbsolutePath():
    """iterate over all files in dir"""
    pathToProject = pathlib.Path(__file__).parent.absolute()
    fullpath = str(pathToProject) + "/" + "files/"     
    print("absolute path to dir with files", fullpath)
    return fullpath


def filesInDir(pathToDir):
    """iterate over all files in dir"""
    dirs = os.listdir( pathToDir )     
    # This would print all the files and directories
    for file in dirs:
        print (file)
    

def main():
    absolutePath = getAbsolutePath()
    # specify file ending, no dot
    createTestData(absolutePath,"md")
    filesInDir(absolutePath)
main()