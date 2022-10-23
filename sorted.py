count=0
def sorted(a) :
    global count
    b = list(a)
    for last in range(len(b)-1,-1,-1) :
        swapped = False
        for i in range(last) :
            if b[i] > b[i+1] :
                b[i], b[i+1] = b[i+1], b[i]
                count+=1
                swapped = True
            else:
                count+=1

        if not swapped :
            break
    if a == b :
        return True
    else :
        return False

inp = [int(i) for i in input('Enter Input : ').split()]
# if sorted(inp) :
#     print("Yes")
# else :
#     print("No")
sorted(inp)
print(inp)
print(count)