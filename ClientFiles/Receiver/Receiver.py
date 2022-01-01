from urllib.request import *
import time
import os
while True:
    time.sleep(2)
    os.system("cls")
    response = urlopen('http://localhost:1111/index.html')
    html = response.read()
    with open("Commands.cpgf","w") as commands:
        commands.writelines(str(html))
    

