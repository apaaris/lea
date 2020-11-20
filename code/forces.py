#TODO calculate forces
lift = []
drag = []
R = []
axis = ['x' ,'y' ,'z']
print('Enter lift and drag forces:')
print('')
print('Lift:')
for i in range(0, 3):
   ele = float(input(axis[i] + ':  '))
   lift.append(ele)
print('Drag: ')
for i in range(0, 3):
   ele = float(input(axis[i] + ':  '))
   drag.append(ele)

for i in range(0,3):
    R.append(lift[i] + drag[i])

print(R)
