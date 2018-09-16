#Follow set
dict ={}
'''
n=int(input('Enter the number of productions'));
for i in range(0,n):
    k=input('Enter the key in capital don't enter complement ');
    v=input('Enter the key give ^ for null  ');
    dict [k]= v;
print(dict)
'''
dict ['E'] = 'TU'
dict ['U'] = '+TU|^'
dict ['T'] = 'FV'
dict ['V'] = '*FV|^'
dict ['F'] = 'i|a'
print('items')
cnt=0;
F1=[]
F2=[]
for g, y in dict.items():
  print(g, y)
  F1.append('')
  F1[cnt]=y.split('|')
  F2.append('')
  F2[cnt]=y
  cnt+=1;
print('F1 -------',F1)
cnt=0;
flw={}
m='$'
for g, y in dict.items():    
  find=0;
  for i in range(0, len(F1)):
    if(F2[i]!=y):
      for j in range(0, len(F1[i])):    
        for k in range(0,len(F1[i][j])):
          if(g is F1[i][j][k]):
            find=1;
            if(k==len(F1[i][j])-1): #last element            
              find=0;
            else:
              z=len(F1[i][j][k+1])  #First of code
              p=F1[i][j][k+1]
              cpeg=0;
              value=2;
              h=[];
              for a,b in dict.items():                
                if(a==p):
                  for i2 in F1[cpeg]:
                    if(i2[0]!='^'):
                      h.append(i2[0])
                    else:
                      if('$' not in h):
                        h.append('$')
                  break;
                cpeg+=1;                  
            print('break',g,'____',F1[i][j],'____',y)
            break;              
        #After BREAK is applied it starts here from '#' position
  if(find==0):
    flw [g] = m
    print('f=0 store in $ flw  ',flw)
  else:
    print('B');
    flw [g] = h
    print('f=1 store in $ flw  ',flw)
  cnt+=1;
print(flw)
