import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logging
from core import Memoadmin


MF= Memoadmin.MA
LF=Memoadmin.L
def main():
 try:
  while True:  #while 循环开始过程
    MF.welcome()
    if sys.argv[1] in {"-h", "--help"}:
      MF.check()
      MF.help()
      break
    elif sys.argv[1] in {"-a", "--add"}:
      MF.check()
      LF.talk()
      xxx= input('你还想干什么(1:add, 2:query, 3: modify, 4:delete,5:save, 6: load):')
      if xxx=='1':
          LF.talk()
      elif xxx=='2':
          MF.query()
      elif xxx=='3':
          MF.modify()
      elif xxx=='4':
          MF.dele()
      elif xxx=='5':
          MF.save()
      elif xxx=='6':
          MF.load()
    elif sys.argv[1] in {"-d", "--delete"}:
      MF.dele()
    elif sys.argv[1] in {"-m", "--modify"}:
      MF.modify()
    elif sys.argv[1] in {"-q", "--query"}:
      MF.query()
    elif sys.argv[1] in {"-s", "--save"}:
      MF.save()
    elif sys.argv[1] in {"-l", "--load"}:
      MF.load()
    else:
        MF.help()

 except Exception as e:
        print(e)

if __name__ == '__main__':
    main()