import os
import sys

pythonexe = os.path.dirname(sys.executable) + "\python.exe"

scriptexe = os.getcwd() + "\SBillMoveRename.py"
print("\nPython.exe path: " + pythonexe)
print("SBillMoveRename.py path: " + scriptexe)
print("Run_Python_Script.bat generated.\n")

f = open("Run_Python_Script.bat","w+")
f.write('"'+pythonexe+'" "'+scriptexe+'"')
f.flush()
f.close()

os.system(r'cmd /k "SCHTASKS /CREATE /SC MINUTE /MO 1 /TN "MyTasks\SBill Task" /TR "' + os.getcwd() + '\Run_Python_Script.bat" /ST 01:05"')


