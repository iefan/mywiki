import os
import conf
import shutil

curdir = os.getcwd()
outputdir = conf.OUTPUT_FOLDER
print outputdir
print curdir

os.chdir(outputdir)
# shutil.rmtree()
filelist = [ f for f in os.listdir(".") ]
for f in filelist:
    if f == ".git":
        print 'git should exist! ======================================'
    else:
        try:
            os.remove(f)
        except:
            shutil.rmtree(f)

os.chdir(curdir)
os.system("nikola build")

os.chdir(outputdir)
# os.system("git pull")
# os.system("git add .")
# os.system("git status")

# os.chdir(outputdir)

# os.system("nikola serve")
