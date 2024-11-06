#Change to base ten
num=input('Number: ')
base=int(input('Base: '))
list=[]
for i in range(len(num)):
    number=int(num[i])
    value=number*(base**(len(num)-i-1))
    print(number,'x',base,'^',len(num)-i-1,'=',value)
    list.append(value)
result=0
for i in list:
    result+=i
print(result)