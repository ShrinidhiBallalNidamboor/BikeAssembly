from Define import readfile
from Define import getfile
from Define import sendgoods
from Define import filepath
from Define import warehouses
import threading

def command():
    readfile(filepath[6])
    while True:
        print('Send items: ')
        commandinput=input('Enter the command(Y/N): ')
        if commandinput=='Y':
            data=getfile(filepath[5])
            data=data.split('\n')
            data=data[-1]
            a, b=data.split('-')
            array=a.split(',')
            length=len(array)
            for i in range(length):
                array[i]=int(array)
            components=[]
            index=0
            for i in warehouses[int(b)]:
                components.append([i, array[index]])
                index+=1
            timer_thread=threading.Timer(30.0, sendgoods, args=('Orders Delivered', int(b), components))
            timer_thread.start()