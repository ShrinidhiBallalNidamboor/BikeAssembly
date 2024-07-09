import time
filepath=[]
filepath.append('../Database/Messenger/Manager1.txt')
filepath.append('../Database/Messenger/Manager2.txt')
filepath.append('../Database/Messenger/Manager3.txt')
filepath.append('../Database/Messenger/Manager4.txt')
filepath.append('../Database/Messenger/Manager5.txt')
filepath.append('../Database/Messenger/Manager6.txt')

filepath.append('../Database/Predetermined/RuleSet.txt')
filepath.append('../Database/Predetermined/Demand.txt')

filepath.append('../Database/Predetermined/Warehouse/Warehouse1.txt')
filepath.append('../Database/Predetermined/Warehouse/Warehouse2.txt')
filepath.append('../Database/Predetermined/Warehouse/Warehouse3.txt')
filepath.append('../Database/Predetermined/Warehouse/Warehouse4.txt')
filepath.append('../Database/Predetermined/Warehouse/Warehouse5.txt')

def warehouse(i, component):
    with open(filepath[i+8], 'r') as file:
        data=file.read()
        data=data.split('\n')
        for j in data:
            a, b=j.split('-')
            b=b.split(',')
            if a==component:
                return [int(b[0]), int(b[1])]
    return None

def storewarehouse(i, component, value):
    array=[]
    with open(filepath[i+8], 'r') as file:
        data=file.read()
        data=data.split('\n')
        for j in data:
            a,b=j.split('-')
            b=b.split(',')
            if a==component:
                array.append(a+'-'+str(value)+','+b[1])
            else:
                array.append(j)
    return None

def notify(message, list):
    for i in list:
        with open(filepath[i], 'a+') as file:
            file.write(message)

def createmessenger():
    for i in range(6):
        with open(filepath[i], 'w') as file:
            file.write('')

def readfile(filepath):
    with open(filepath, 'r') as file:
        data=file.read()
        return data

def sendgoods(msg, to, components):
    notify(msg, [to])
    for i in components:
        value=warehouse(to,i[0])[0]+i[1]
        storewarehouse(to,i[0],value)

def command(i,next,list):
    print(readfile(filepath[6]))
    while True:
        print('1. Order Products from shop')
        print('2. Send finished products')
        print('3. Assemble or paint')
        print('4. Check warehouse')
        print('5. Exit')
        commandinput=input('Enter the command: ')
        if commandinput=='1':
            print('Items available in the shop:')
            print(readfile(filepath[i+8]))
            order=input('Enter the quantity of items needed for each item separate by commas: ')
            notify(order+'-'+str(i)+'\n', [4])
            print('Order Placed')
        elif commandinput=='2':
            val=[]
            for j in list:
                val.append([j[0],warehouse(0,j[0])[0]])
            time.sleep(10)
            sendgoods('Ordered Goods delivered', next, val)
            for j in list:
                storewarehouse(i,j[0],0)
            print('Goods transferred')
        elif commandinput=='3':
            val=[]
            for j in list:
                minimum=[]
                for k in j[1]:
                    minimum.append(warehouse(i,k)[0]//warehouse(i,k)[1])
                minimum=min(minimum)
                val.append([j[0],warehouse(i,j[0])[0]+minimum])
            for j in val:
                storewarehouse(i,j[0],j[1])
        elif commandinput=='4':
            print('Warehouse: ')
            print(readfile(filepath[i+8]))
        else:
            break