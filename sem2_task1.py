sp = []
sp.append(True) 
#добавление списка с помощью .append
sp = sp + [5467, 245, 'Артем', [4, 5, 6, 7] ]
print(sp)
sp.insert(0, 999) 
#добавление нового символа, сначала указывается индекс постановки и полсе сам объект .insert
print('after insert', sp)

print(sp[-1] [-1])

a = sp.pop(-1) 
#вырезка объекста из одной переменной с указанием его индекса объекта и добавление его в новую переменную с присвоением .pop
print('after pop', a)

#a.remove(2) #удаление определённого объекта из списка .remove
#print('after remove', a)

#как проходиться по всем спискам 
for i in a: print(i)


#двумерные списки, создание
mas_2dim = []
for i in range(5):
    temp =[]
    for j in range(5):
        temp.append(i + j)
        mas_2dim.append(temp)

for i in range(len(mas_2dim)):
    print(mas_2dim[i])