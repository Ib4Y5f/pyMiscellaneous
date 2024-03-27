print(dir())
import os
print('Libraries after importing os')
print(dir())
import datetime
print('Libraries after importing datetime')
print(dir())
print("time now: ", datetime.datetime.now())
username=os.environ["USERNAME"]
computername=os.environ["COMPUTERNAME"]
print("PC name is: ", computername)
print("username on PC is: ", username)

