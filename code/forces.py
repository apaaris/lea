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


def distance(r1, r2):
    lst = []
    for i in range(0, 3):
        lst.append(r2[i]-r1[i])
    return lst


def resultant(f1, f2):
    lst = []
    for i in range(0, 3):
        lst.append(f1[i]+f2[i])
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
    delta = distance(m_p, c_p)
    r_tot = resultant(lift, drag)
    torque = cross(delta, r_tot)
    return 0


main()
