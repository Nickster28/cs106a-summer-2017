#!/usr/bin/env python

'''
FILE: compile.py
----------------
Template compiler that compiles all .html template files in the TEMPLATE_DIR
directory below (excluding .ptl files, which are partial templates), and outputs
with the same filenames to the OUTPUT_DIR directory.  Use -t to compile for
running locally; otherwise, templates are compiled to be hosted at the ROOT url.
Example usage:

> python compile.py -t --output_dir WWW

Compiles all template files using local paths, and outputs the compiled files to
the WWW directory.  The compiled files in WWW/ have the same directory structure
as in the TEMPLATE_DIR directory.

> python compile.py

Compiles all template files using ROOT path, and outputs the compiled files to
the *current* directory.  The compiled files in the current directory have the
same directory structure as in the TEMPLATE_DIR directory.
----------------
'''

import os.path
from bottle.bottle import SimpleTemplate
import sys
import json
import courseInfo

TEMPLATE_DIR = 'templates'

# Assumed to be within OUTPUT_DIR
HANDOUTS_DIR = 'handouts'

# The root URL at which this webpage is hosted
ROOT = '//web.stanford.edu/class/archive/cs/cs106a/cs106a.' + str(courseInfo.QUARTER_NUMBER) + '/'

# Use the -t flag if you want to compile for local tests
DEPLOY = not '-t' in sys.argv

# Use the --output_dir flag to optionally specify where compiled files go
if '--output_dir' in sys.argv:
    OUTPUT_DIR = sys.argv[sys.argv.index('--output_dir') + 1]
else:
    OUTPUT_DIR = 'WWW'

'''
FUNCTION: compile
-----------------
Parameters: NA
Returns: NA

This function compiles all the html files (recursively)
from the templates dir into the current folder. Folder
hierarchy is preserved.
-----------------
''' 
def compile():
    # Read in the syllabus files
    with open('schedule.json') as scheduleFile:
        scheduleData = json.load(scheduleFile)
        handoutsData = searchHandoutsDirectory()

        # Compile all templates
        templateFilePaths = getTemplateFilePaths('')
        print("\nCompiling:\n----------")
        for templateFilePath in templateFilePaths:
            print("Compiling " + templateFilePath + "...")
            outputPath = compileTemplate(templateFilePath, scheduleData,
                handoutsData)
            print(templateFilePath + " -> " + outputPath)

    print("\nDONE.\n")

'''
FUNCTION: searchHandoutsDirectory
---------------------------------
Parameters: NA
Returns: a list of tuples containing information about the handouts in
OUTPUT_DIR/HANDOUTS_DIR.  In particular, the tuples are of the format
(handout name, URL).
---------------------------------
'''
def searchHandoutsDirectory():
    handoutsData = []
    handoutsDirPath = OUTPUT_DIR + '/' + HANDOUTS_DIR + '/'
    for fileName in os.listdir(handoutsDirPath):
        filePath = os.path.join(HANDOUTS_DIR, fileName)
        if fileName == "assignments" or fileName.startswith("."):
            continue

        # The name is found by separating each dashed word in the filename
        # except for the first, which is the handout number.  E.g.
        # 1-General-Information.pdf -> 1-General Information
        nameList = os.path.splitext(fileName)[0].split('-')
        handoutName = nameList[0] + ' - ' + ' '.join(nameList[1:])

        handoutsData.append((handoutName, filePath))
        handoutsData.sort(key=lambda x: x[0])

    return handoutsData 


'''
FUNCTION: getTemplateFilePaths
------------------------------
Parameters:
    templateRoot - the folder within TEMPLATE_DIR to get file paths for

Returns: a list of .html template file paths from within the given directory
within TEMPLATE_DIR.  Ignores .ptl files, which are partial templates.
------------------------------
'''
def getTemplateFilePaths(templateRoot):
    paths = []
    templateDirPath = os.path.join(TEMPLATE_DIR, templateRoot)
    for fileName in os.listdir(templateDirPath):
        filePath = os.path.join(templateRoot, fileName)
        templateFilePath = os.path.join(TEMPLATE_DIR, filePath)

        # Recurse if it's a directory, add if it's a template file
        if os.path.isdir(templateFilePath):
            childPaths = getTemplateFilePaths(filePath)
            for childPath in childPaths:
                paths.append(childPath)
        elif isTemplateFile(fileName):
            paths.append(filePath)

    return paths

'''
FUNCTION: isTemplateFile
------------------------
Parameters:
    fileName - the fileName to check is a template file

Returns: whether or not the given filename is a template file (ends with .html)
------------------------
'''
def isTemplateFile(fileName):
    extension = os.path.splitext(fileName)[1]
    return extension == '.html'

'''
FUNCTION: compileTemplate
-------------------------
Parameters:
    relativePath - the path within TEMPLATE_DIR of the template file to compile
    scheduleData - the JSON object containing schedule data.  Passed in as a
                    parameter to render the template.
    handoutsData - the list of tuples of handout data.  Passed in as a parameter
                    to render the template.

Returns: the path of the saved, compiled template file.

Compiles the given template file, passing in the pathToRoot, scheduleData,
and handoutsData as template parameters.  Saves the compiled
template to relativePath in the OUTPUT_DIR directory.
-------------------------
'''
def compileTemplate(relativePath, scheduleData, handoutsData):
    pathToRoot = getPathToRootFrom(relativePath)
    filePath = os.path.join(TEMPLATE_DIR, relativePath)
    templateText = open(filePath).read()
    compiledHtml = SimpleTemplate(templateText).render(pathToRoot=pathToRoot,
        schedule=scheduleData, handouts=handoutsData, courseInfo=courseInfo)
    compiledHtml = compiledHtml.encode('utf8')

    relativePath = os.path.join(OUTPUT_DIR, relativePath)
    makePath(relativePath)
    open(relativePath, 'wb').write(compiledHtml)
    return relativePath

'''
FUNCTION: getPathToRootFrom
---------------------------
Parameters:
    relativePath - the path to start at when calculating the path to the root

Returns: the path to the root directory from the given relativePath.
---------------------------
'''
def getPathToRootFrom(relativePath):
    if DEPLOY:
        return ROOT
    return getRelPathToRootFrom(relativePath)

'''
FUNCTION: getRelPathToRootFrom
------------------------------
Parameters:
    relativePath - the path to start at when calculating the path to the root

Returns: the relative path to the root directory from the given relativePath.
    Concatenates "../" for each level down from the root.
------------------------------
'''
def getRelPathToRootFrom(relativePath):
    depth = depthFromRoot(relativePath)
    pathToRoot = './' + ''.join(['../' for i in range(depth)])
    return pathToRoot

'''
FUNCTION: depthFromRoot
-----------------------
Parameters:
    filePath - the path for which to calculate the depth

Returns: the number of levels filePath is from the root level.
    E.g. 'index.html' -> 0
         'stuff/index.html' -> 1
         'stuff/moreStuff/index.html' -> 2
-----------------------
'''
def depthFromRoot(filePath):
    rootPath = os.path.dirname(filePath)
    if len(rootPath) == 0: return 0
    return depthFromRoot(rootPath) + 1
    
'''
FUNCTION: makePath
------------------
Parameters:
    path - the path to make directories for

Returns: NA

Creates all needed directories in this path for the directory path to exist.
E.g. if path = 'stuff/moreStuff/index.html' then the stuff and moreStuff
directories would be created if they did not already exist.
------------------
'''
def makePath(path):
    dirPath = os.path.dirname(path)
    if dirPath != '' and not os.path.exists(dirPath):
        os.makedirs(dirPath)


if __name__ == '__main__':
    compile()
