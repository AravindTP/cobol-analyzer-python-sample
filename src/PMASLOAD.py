# Load all files with Name and Line Number

import os
import glob
import re
import mysql.connector
from mysql.connector import errorcode
from time import localtime, strftime

path=(r'C:\Users\aravind-t\Desktop\')

try:
    cnx = mysql.connector.connect(user='root', password='Password',
                                    host='127.0.0.1',
                                    database='Vanguard')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
StartTime = localtime()
print(StartTime)
current_ts = strftime("%Y-%m-%d %H:%M:%S", localtime())
cursor1 = cnx.cursor()
add_SearchResult = ("INSERT INTO Inventory "
                    "(LanType, FilName, Content, LineNum, ConType, CreatTS) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")

for filenames in glob.glob(os.path.join(path, '*.txt')):
    print("path is " + path)
    FolderName = os.path.basename(path)

    if len(FolderName) > 8:
        CompType = FolderName[:8]
    else:
        CompType = FolderName
                    
    if os.path.isfile(filenames):
        filename = os.path.basename(filenames)
        NoExtnFile = os.path.splitext(filename)[0]
        Lno = 0
        with open (filenames,"r",encoding='UTF') as InpF:

            for EachLine in InpF:
                EachLin=EachLine[0:80]
                print(EachLin)
                Lno = Lno + 1
                CType = " "
                current_ts = strftime("%Y-%m-%d %H:%M:%S", localtime())
                data_SearchResult = (CompType, NoExtnFile, EachLin, Lno, CType, current_ts )
                cursor1.execute(add_SearchResult,data_SearchResult)
                    
        print("Last processed file is " + NoExtnFile)
        cnx.commit()

cursor1.close()
cnx.close()
EndTime = localtime()
print(EndTime)
