g = int(input())
nv1 = g % 400
nv2 = g % 100
nv3 = g % 4
if nv1 == 0 and nv2 > 0:
    print('yes')
if nv3 == 0:
    print('yes')
else:
    print('no')