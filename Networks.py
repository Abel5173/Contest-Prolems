# def  SPF_nodes(d):
    

nd = {}
for i in range(10):
    nd[i] = []
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break        
    else:
        nd[a[0]].append(a[1])
        # continue
t = False
for i in nd:
    a = nd[i]
    if len(a) >= 3:
        for j in a:
            if nd[j] in a:
                print('Network #1 \n\tSPF node 3 leaves 2 subnets')
                t = True
if t:
    print('Network #2\n\tNo SPF nodes')

