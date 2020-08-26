my_dict = {'x':5000, 'y':5873, 'z':560}

min_value = min(my_dict.keys() , key=lambda k: my_dict[k])
max_value = max(my_dict.keys() , key=lambda k: my_dict[k])

print("Minimum value :" , my_dict[min_value])
print("Maximum value :" , my_dict[max_value])


