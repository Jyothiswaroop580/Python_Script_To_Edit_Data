from random import randrange
valu=input()
columns=[]
data=[]
count=0
count2=0
f = open('E:\Office midtree\Shneider\insertion.txt')
print("\n")
for word in f.read().split(','):
    if word == ') values (':
        count+=1
        continue
    if word == valu or word ==');':
        pass
    else:
        if count>=1:
            data.append(word)
        else:
            columns.append(word)
print(columns)
print(data)

f = open("E:\Office midtree\Shneider\data types.txt", 'r')
data_types = {}
for line in f:
    k, v = line.strip().split(',')
    data_types[k.strip()] = v.strip()
f.close()

for i in columns:
    data_type_temp=data_types[i]
    if data_type_temp=='Number':
        data[count2]=randrange(9)
    elif data_type_temp=='Varchar':
        data[count2]="Test"#+str(randrange(9))
    elif data_type_temp=='Float':
        data[count2]=float(randrange(9))
    count2+=1
print(columns)
print(data)

file = open('E:\Office midtree\Shneider\edited.txt','w')
file.writelines(valu)
for i in range(len(columns)-1):
    if i!=0:
        file.writelines(','+columns[i])
    else:
        file.writelines(columns[i])
file.writelines(') values (')
for i in range(len(columns)-1):
    if i!=0:
        file.writelines(','+str(data[i]))
    else:
        file.writelines(str(data[i]))
file.writelines(')')
#file.writelines(data)
file.close()