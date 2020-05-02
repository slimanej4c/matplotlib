ville=['bba','setif']
contry=['algeria','tenus']


m = [[i for i in range(3)] for j in range(3)]
m = {k: v for k, v in enumerate(ville)}
f = {k: v for k, v in zip(contry, ville)}
print(f)
print(m)
for i, j in zip(contry, ville):
    print(i)
    print(j)

d={'nigative':[-5,-6],'posifive':[]}
ni=[[],[]]
sign=['positive','nigative']
def claser(d,*args):

    for vv in args[0]:
        for v in vv:
            if v > 0:
                d['nigative'].append(v)
                ni[1].append(v)
            else:
                d['posifive'].append(v)
                ni[0].append(v)
    b = {k: v for k, v in zip(sign, ni)}
    return b

l=[[9,5,9,-5,9,-1,-7,8,-10,6],[9,5,9,-5,9],[1,1,1,-1,-1,-1]]

claser(d,l)
print(claser(d,l))

nigative=[[-1,-5,-6],[1,5,7]]



b={k:v for k,v in zip(sign,nigative)}
#print(b)

a=9
b=3
if a//3==0:
    print('ok')