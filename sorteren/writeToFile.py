from time import sleep
from pathlib import Path

dataDir=Path("./datadir")
fileName=dataDir / "test.txt"
file=open(fileName, 'w')
file.close()

counter=0
while True:
    file=open(fileName, 'a')
    file.write(str(counter)+"\n")
    file.close()
    print(f"Writing {counter} in file")
    counter +=1
    sleep(1)
    

    
    
    
    


