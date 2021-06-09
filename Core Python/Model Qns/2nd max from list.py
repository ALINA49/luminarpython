list=[26,56,78,90,89,100,99,45,23,12,1,9,78]
new_list=set(list)
new_list.remove(max(new_list))
print(max(new_list))