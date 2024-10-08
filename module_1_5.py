tuple_= 'immutable_var:'
print(tuple_)
tuple_2=(1, 2, 3, 4, 5)
print(tuple_2[0])
tuple_3=(1, 2, 3, 4, 5)
print(tuple_3[1])
tuple_= 'immutable_var:'
print(tuple_[5])
print(tuple_[6])
# tuple_[0]=100 # или будь то буквы объект 'str' не поддерживает назначение элемента. tuple_- то есть кортеж, придуман для хранилища и чтобы он оставался неизменным.
name= ['mutable_list:']
print (name)
name= mutable_list =(1, 2, 3, 4, 5)
print (name)
name=(1, 2, 3, 4, 5)
print(name[0])
print(name[1])
name= ['mutable_list:']
print (name)
name.extend("ab")
print (name)
name.append('Modified')
print (name)



