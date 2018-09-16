num=int(input('Enter the number of productions:'))
lr=0
final=list()
for l in range(num):
    print('Enter production ',l,' :')
    gram=input()
    temp=list()
    alpha=list()
    beta=list()
    temp.append(gram[0])
    i=''
    temp.append(gram[3:])
    i=temp[0]
    if((temp[1].find('|'))!=-1):
        temp[1]=temp[1].split('|')
        
    
    for prod in temp[1]:
        
        if((prod.find(i)==0)):
            alpha.append(prod[1:])
            lr+=1
        else:
            beta.append(prod)
    if(lr!=0):
        
        newgram=''
        newgram=i+'->'
        for j in beta:
            newgram+=(j+i+'\''+'|')
    
        newgram=newgram[:-1]
        newgram1=''
        newgram1=i+'\''+'->'
        for j in alpha:
            newgram1+=(j+i+'\''+'|')
        newgram1+='epsilon'
        
        final.append(newgram)
        final.append(newgram1)
    else:
        final.append(gram)
    lr=0

print('Removing left recursion:')
for i in final:
    print(i)


    
