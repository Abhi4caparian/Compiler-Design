num=int(input('Enter number of productions:'))
final=list()
for l in range(num):
    print('Enter production ',l+1,' :')
    gram=input()
    t=0
    flag=1
    while(flag!=2):
        print('T:',t)
        temp=list()
        temp.append(gram[0])
        temp.append(gram[3:])
        if((temp[1].find('|'))!=-1):
            temp[1]=temp[1].split('|')
        s=temp[0]
        
        alpha=''
        a1=list()
        alpha=temp[1][1]
        while(flag!=0):
            gamma=list()
            beta=list()
            calpha=0
            for prod in temp[1]:
                
                if(prod.find(alpha)!=-1):
                    if(prod[len(alpha):]==''):
                        app='epsilon'
                    else:
                        app=prod[len(alpha):]
                    beta.append(app)
                    calpha+=1
                else:
                    gamma.append(prod)
                
            if(calpha>1):
                flag=0
            else:
                alpha=alpha[:-1]
        print('Alpha:',alpha)
        print('Beta:',beta)
        print('Gamma',gamma)
            
        flag=1
        if(alpha==''):
            flag=2
            final.append(gram)
        else:
            prev=0
            s=temp[0]
            for i in range(t+1):
                s+='\''
            newgram=''
            newgram=temp[0]+'->'
            newgram+=(alpha+s+'|')
            
            for i in gamma:
                    newgram+=(i+'|')
            newgram=newgram[:-1]
            newgram1=''
            newgram1+=(s+'->')
            for i in beta:
                newgram1+=(i+'|')
            newgram1=newgram1[:-1]
            final.append(newgram1)
            gram=newgram
        print('next Gram:',newgram)
        print('final Gram:',newgram1)
        t+=1
        i=len(final)-1
        while(i!=-1):
            print(final[i])
            i-=1
                
            
                

                    
    
            
                
            
        
        
    
    
    
    
