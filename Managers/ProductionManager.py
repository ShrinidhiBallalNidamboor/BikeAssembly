from Define import createmessenger
from Define import readfile
from Define import notify
from Define import warehouse
from Define import filepath
from Define import warehouses


try:
    createmessenger()
    warehouse()
    readfile(filepath[6])
    readfile(filepath[7])
    print('Bikes in warehouse is '+warehouses[4]['Bike'][0])
    target=input('Enter the target: ')
    notify('Target for the day is '+target, [0, 1, 2, 3]) 
    print('Target was successfully broadcasted')       
except:
    print('An error occurred during the processing of the orders')