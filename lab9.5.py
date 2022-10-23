inp = input('Enter Input : ').split('/')
print('== results ==')
ans = []
for ele in inp:
    lst=[]
    d1={}
    d2={}
    ele = ele.split(',')
    point=0
    point += int(ele[1])*3
    point += int(ele[3])
    gd = int(ele[4])-int(ele[5])
    d1['points'] = point
    d2['gd'] = gd
    lst.append(ele[0])
    lst.append(d1)
    lst.append(d2)
    ans.append(lst)

def bubblesort(list):
   for ele in range(len(list)-1,0,-1):
      for idx in range(ele):
        if list[idx][1]['points']<list[idx+1][1]['points']:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
        elif list[idx][1]['points']==list[idx+1][1]['points']:
            if list[idx][2]['gd']<list[idx+1][2]['gd']:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
bubblesort(ans)
for ele in ans:
    print(ele)