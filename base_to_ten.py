#Change to base ten
num=input('Number: ')
asas=int(input('Asas: '))
list=[]
for i in range(len(num)):
    number=int(num[i])
    value=number*(asas**(len(num)-i-1))
    print(number,'x',asas,'^',len(num)-i-1,'=',value)
    list.append(value)
result=0
for i in list:
    result+=i
print(result)