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
            print('Items available in the shop:', warehouses[3])
            order=input('Enter the quantity of items needed for each item separate by commas: ')
            notify(order+'-'+'3\n', [4])
            print('Order Placed')
        elif commandinput=='2':
            timer_thread=threading.Timer(30.0, sendgoods, args=('Bike delivered '+str(warehouses[3]['Bike'][0]), 5, [['Bike', warehouses[3]['Bike'][0]]]))
            timer_thread.start()
            warehouses[3]['Bike'][0]=0
            print('Goods transferred')
        elif commandinput=='3':
            warehouses[3]['Bike'][0]+=min([warehouses[3]['BikeFramePainted'][0]//warehouses[3]['BikeFramePainted'][1],warehouses[3]['Tyre'][0]//warehouses[3]['Tyre'][1],warehouses[3]['Screw'][0]//warehouses[3]['Screw'][1]])
        else:
            print('Warehouse: ', warehouses[2])