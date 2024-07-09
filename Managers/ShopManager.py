from Define import readfile
from Define import getfile
from Define import sendgoods
from Define import filepath
import threading

print(readfile(filepath[6]))
while True:
    print('Send items: ')
    commandinput=input('Enter the command(Y/N): ')
    if commandinput=='Y':
        data=getfile(filepath[5])
        data=data.split('\n')
        if data==[]:
            continue
        data=data[-1]
        a,b=data.split('-')
        array=a.split(',')
        components=[]
        length=len(array)
        result=readfile(filepath[int(b)+8]).split('\n')
        for i in range(length):
            components.append([result[i].split('-')[0], int(array[i])])
        timer_thread=threading.Timer(30.0, sendgoods, args=('Orders Delivered', int(b), components))
        timer_thread.start()
    else:
        break