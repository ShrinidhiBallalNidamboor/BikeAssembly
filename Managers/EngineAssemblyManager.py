from Define import readfile
from Define import notify
from Define import sendgoods
from Define import filepath
from Define import warehouses
import threading

def command():
    readfile(filepath[6])
    while True:
        print('1. Order Products from shop')
        print('2. Send finished products')
        print('3. Assemble or paint')
        print('4. Check warehouse')
        commandinput=input('Enter the command: ')
        if commandinput=='1':
            print('Items available in the shop:', warehouses[1])
            order=input('Enter the quantity of items needed for each item separate by commas: ')
            notify(order+'-'+'1\n', [4])
            print('Order Placed')
        elif commandinput=='2':
            timer_thread=threading.Timer(30.0, sendgoods, args=('Ordered Goods delivered', 2, [['BikeFrame', warehouses[1]['BikeFrame'][0]]]))
            timer_thread.start()
            warehouses[1]['BikeFrame'][0]=0
            print('Goods transferred')
        elif commandinput=='3':
            warehouses[1]['BikeFrame'][0]+=min([warehouses[1]['Frame'][0]//warehouses[1]['Frame'][1],warehouses[1]['Engine'][0]//warehouses[1]['Engine'][1]])
        else:
            print('Warehouse: ', warehouses[1])