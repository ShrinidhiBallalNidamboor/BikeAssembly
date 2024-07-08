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

warehouses={}
warehouses[0]={}
warehouses[1]={}
warehouses[2]={}
warehouses[3]={}

def warehouse():
    for i in range(5):
        with open(filepath[i+7], 'r') as file:
            data=file.read()
            data=data.split('\n')
            for j in data:
                a, b=j.split('-')
                b=b.split(',')
                warehouses[i][a]=[int(b[0]), int(b[1])]

def notify(message, list):
    for i in list:
        with open(filepath[i], 'a+') as file:
            file.write(message)

def createmessenger():
    a=filepath[0]
    b=filepath[1]
    c=filepath[2]
    d=filepath[3]
    with open(a, 'w') as file:
        file.write('')
    with open(b, 'w') as file:
        file.write('')
    with open(c, 'w') as file:
        file.write('')
    with open(d, 'w') as file:
        file.write('')

def readfile(filepath):
    with open(filepath, 'r') as file:
        data=file.read()
        print(data)

def getfile(filepath):
    data=''
    with open(filepath, 'r') as file:
        data=file.read()
        return data

def sendgoods(msg, to, components):
    notify(msg, [to])
    for i in components:
        try:
            warehouses[to][i[0]][0]+=i[1]
        except:
            print('',end='')