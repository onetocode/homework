x1 = int(input('Введите координату x1:'))
y1 = int(input('Введите координату y1:'))
x2 = int(input('Введите координату x2:'))
y2 = int(input('Введите координату y2:'))
x3 = int(input('Введите координату x3:'))
y3 = int(input('Введите координату y3:'))
X1 = x2 - x1
Y1 = y2 - y1
X2 = x3 - x1
Y2 = y3 - y1
X3 = x3 - x2
Y3 = y3 - y2
O1 = X1 * X1 + Y1 * Y1
if O1 < 0:
    O1 = O1 * -1
O2 = X2 * X2 + Y2 * Y2
if O2 < 0:
    O2 = O2 * -1
O3 = X3 * X3 + Y3 * Y3
if O3 < 0:
    O3 = O3 *-1
if O1 == O2 + O3:
    print('yes')
if O2 == O3 + O1:
    print('yes')
if O3 == O1 + O2:
    print('yes')
if O1 != O2 + O3 and O2 != O3 + O1 and O3 != O1 + O2:
    print('no')