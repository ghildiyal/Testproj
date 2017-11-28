import os
import subprocess

class changeDir:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  # Change directory with the new path
  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  # Return back to previous directory
  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)

# folderPath = path of the folder you want to run mvn clean install on
with changeDir("C:\\Foundation IP Code\\code"):
  # ****** NOTE ******: using shell=True is strongly discouraged since it possesses security risks
  #subprocess.call(["mvn", "clean", "install"], shell=True)
  #subprocess.call(["mvn", "dependency", ":", "resolve"], shell=True)
# os.chdir("C:\\dependency-check\\bin")
command=subprocess.run('dependency-check.bat --project Akhil --scan C:\\New\\AKHIL\\lib', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print(command)



