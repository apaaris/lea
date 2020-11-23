# To Do: Beautify output
axis = ['x', 'y', 'z']


def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c


def enter():
    lst = []
    for i in range(0, 3):
        lst.append(float(input(axis[i] + ':  ')))
    return lst


def resultant(f1, f2, sign):
    lst = []
    if sign == 1:
        for i in range(0, 3):
            lst.append(f1[i]+f2[i])
    else:
        for i in range(0, 3):
            lst.append(f2[i]-f1[i])
    return lst


def main():
    print('Enter lift and drag forces: [N]')
    print('Lift:')
    lift = enter()
    print('Drag: ')
    drag = enter()
    print('Enter position of Center of Pressure: [m]')
    c_p = enter()
    print('Enter midpoint of shaft surface: [m]')
    m_p = enter()
    delta = resultant(m_p, c_p, 0)
    r_tot = resultant(lift, drag, 1)
    torque = cross(delta, r_tot)
    print(str(delta) + '  ' + str(torque))
    return 0


main()
