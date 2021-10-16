A = int(input())
B = int(input())

cond_1 = A % 2 != 0
cond_2 = B % 2 != 0

if cond_1 and cond_2:
    print("True")
else:
    print("False")
 # или cond_1 = A % 2 == 0, cond_2 = B % 2 == 0 if not (cond_1 and cond_2)