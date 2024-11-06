#Change to base ten to other base
num=int(input('Nombor asas sepuluh: '))
asas=int(input('Tukar kepada asas: '))
list=[]
print(num)
while num!=0:
    print(num//asas,'-',num%asas)
    list.insert(0,num%asas)
    num=num//asas
for i in list:
    print(i,end='')
print()