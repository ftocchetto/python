my_list = ["One","Two","Three"]
new_list = ["Four", "Five"]
super_list = my_list + new_list
print(len(my_list))
print(my_list[0])
print(super_list)

# adicionando

super_list.append("Six")
print(super_list)

#mudando um elemento na lista

super_list[1] = "Dois"
print(super_list)

# removendo itens da lista
# super_list.pop()
pop_item = super_list.pop(2)
print(pop_item)
print(super_list)

# sort
print("sort \n")
num_list = [1, 3, 6, 8, 2, 4, 7]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
