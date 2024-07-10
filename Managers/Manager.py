from Define import command

print('1. Machine Manager')
print('2. Engine Assembly Manager')
print('3. Painting Assembly Manager')
print('4. Vehicle Assembly Manager')

commandinput=input('Enter the type: ')
if commandinput=='1':
    command(0,1,[['Engine',['Battery','Wire','Piston']],['Frame',['UpperPlate','BottomPlate']]])
elif commandinput=='2':
    command(1,2,[['BikeFrame',['Engine','Frame']]])
elif commandinput=='3':
    command(2,3,[['BikeFramePainted',['BikeFrame','Paint']]])
else:
    command(3,5,[['Bike',['BikeFramePainted','Screw','Tyre']]])


