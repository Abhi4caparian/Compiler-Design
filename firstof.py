# first of
n="S->AB"
m="A->a|^"
o="B->b|^"
print(n)
print(m)

base1=n.split('->')
print(base1)
base2=m.split('->')
print(base2)
base3=o.split('->')
print(base3)

sub1=base1[1]
sub2=base2[1]
sub3=base3[1]
print('sub')
print(sub1)
print(sub2)
print(sub3)

print('Base')
b1=base1[0]
b2=base2[0]
b3=base3[0]
print(b1)
print(b2)
print(b3)

F1=sub1.split('|')
print('F1',F1)

F2=sub2.split('|')
print('F2',F2)

F3=sub3.split('|')
print('F3',F3)

First1=[]
First2=[]
First3=[]
print(First1)

for i in range(0,len(F1)):
    if (F1[i][0] not in First1 and F1[i][0]!=b1):        
        print('----',F1[i][0])
        First1.append(F1[i][0])

for i in range(0,len(F2)):
    if (F2[i][0] not in First2 and F2[i][0]!=b2):
        First2.append(F2[i][0])
        print(F2[i][0])

for i in range(0,len(F3)):
    if (F3[i][0] not in First3 and F3[i][0]!=b3):
        First3.append(F3[i][0])
        print(F3[i][0])
print('first[]')
print(First1)
print(First2)
print(First3)

for i in First1:    
    if(i==b2):
        print(i)
        for j in First2:
            if (j not in First1):
                First1.append(j)
    if(i==b3):
            print(i)
            for j in First3:
                if (j not in First1):
                    First1.append(j)
    
for i in First2:
    if(i==b1):
        print(i)
        for j in First1:
            if (j not in First2):
                First2.append(j)
    if(i==b3):
        print(i)
        for j in First3:
            if (j not in First2):
                First2.append(j)
for i in First3:
    if(i==b1):
        print(i)
        for j in First1:
            if (j not in First3):
                First3.append(j)
    if(i==b2):
        print(i)
        for j in First2:
            if (j not in First3):
                First3.append(j)

                
print('First('+b1+')= ',First1)
print('First('+b2+')= ',First2)
print('First('+b2+')= ',First3)
