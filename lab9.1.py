lst = [int(i) for i in input('Enter Input : ').split()]

for loop in range(1, len(lst)):
    moveNum = None      
    swap = False        

    for i in range(len(lst) - loop):  
        if lst[i] > lst[i + 1]:                     
            moveNum = lst[i]                          
            lst[i], lst[i + 1] = lst[i + 1], lst[i]     
            swap = True                                 
    if loop <= len(lst) - 1 and swap is False:          
        print('last step :', lst, f'move[{moveNum}]')     
        break
    elif loop == len(lst) - 1:
        print('last step :', lst, f'move[{moveNum}]')
    else:                                               
        print(f'{loop} step :', lst, f'move[{moveNum}]')