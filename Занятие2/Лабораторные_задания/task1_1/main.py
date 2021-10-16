a = int(input())

cond_1 = a % 2 == 0       # a крвтно 2
cond_2 = a % 3 == 0       # а кратно 3

if cond_1 or cond_2:      # будет истина если а кратно или двум, или трем, или и двум и трем
    print("True")
else:
    print("False")