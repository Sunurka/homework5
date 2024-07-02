immutable_var = "Sunur",7,True
print(immutable_var)
#кортежи являются не изменяемым типом значения элемента например:
#immutable_var [1] = 100
#print(immutable_var)
#программа даст ошибку если её запустить но, если добавить скобки []
#или через команду: immutable_var=list(immutable_var) изменить значение переменной
#и сделать её списком то она будет работать:
immutable_var = "Sunur",7,True
print(immutable_var)
immutable_var=list(immutable_var) # теперь её можно изменить
immutable_var [1] = 100
print(immutable_var)
print(type(immutable_var)) #или
immutable_var [0] = 5
print(immutable_var)
mutable_list = ['sunur',777,False]
print(mutable_list)
mutable_list [0] = 'ruslan'
mutable_list [1] = 888
mutable_list [2] = True
print(mutable_list)