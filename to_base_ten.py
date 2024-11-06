#Change to base ten to other base
num=int(input('Number in base ten: '))
base=int(input('Change to base: '))
list=[]
print(num)
while num!=0:
    print(num//base,'-',num%base)
    list.insert(0,num%base)
    num=num//base
for i in list:
    print(i,end='')
print()