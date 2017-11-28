import os
import subprocess

os.chdir("C:\\Foundation IP Code\\code")
#command=os.popen('mvn dependency:resolve',shell=TRUE)
command=subprocess.call(["mvn","dependency",":","resolve"],shell=True)
print(command)

# os.chdir("C:\\dependency-check\\bin")
#command=subprocess.run('dependency-check.bat --project Akhil --scan C:\\New\\AKHIL\\lib', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print(command)





