D=int(input())
E=int(input())
A=int(input())
B=int(input())
C=int(input())
for i in range(1):
    if D*E==A*B:
        print('Да')
    else:
        print('Нет')
    if D*E==A*C:
        print('Да')
    else:
        print('Нет')
    if D*E==B*C:
        print('Да')
    else:
        print('Нет')