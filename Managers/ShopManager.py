from Define import readfile
from Define import getfile
from Define import sendgoods
from Define import warehousecomponents
from Define import filepath
import threading

readfile(filepath[6])
while True:
    print('Send items: ')
    commandinput=input('Enter the command(Y/N): ')
    if commandinput=='Y':
        data=getfile(filepath[5])
        data=data.split('\n')
        data=data[-1]
        a,b=data.split('-')
        array=a.split(',')
        components=[]
        index=0
        for i in warehousecomponents(int(b)):
            components.append([i, int(array[index])])
            index+=1
        timer_thread=threading.Timer(30.0, sendgoods, args=('Orders Delivered', int(b), components))
        timer_thread.start()