import PyInstaller.__main__
import datetime
import glob
import os
from sys import platform
from shutil import copyfile, copy, make_archive


orgName = 'The Orange Toolbox'
url = 'https://github.com/The-Orange-Toolbox/AutoCube'
exeName = 'AutoCube'
builddate = datetime.datetime.now().strftime('%b %d %Y')
version = "1.0.0"
distDir = './dist/' + exeName + '-v' + str(version)
exeDir = distDir + '/' + exeName
iconPath = './icon/icon.ico'

# Write version info into _constants.py resource file
with open('src/_constants.py', 'w') as f:
    f.write("ORGNAME = \"{}\"\n".format(orgName))
    f.write("NAME = \"{}\"\n".format(exeName))
    f.write("VERSION = \"{}\"\n".format(version))
    f.write("BUILD_DATE = \"{}\"\n".format(builddate))
    f.write("URL = \"{}\"\n".format(url))

args = ['src/__main__.py',
        '-p', 'src',
        '-n', exeName,
        '-F',
        '--distpath', exeDir,
        '--icon', iconPath]

# Build!
PyInstaller.__main__.run(args)

# Copy other bundle files
copyfile('./README.md', distDir + '/readme.txt')
copy('./plugins/compilepal/meta.json', exeDir)
copy('./plugins/compilepal/parameters.json', exeDir)

# Zip the package
try:
    os.remove(distDir + '.zip')
except OSError:
    pass
make_archive(distDir, 'zip', distDir)
