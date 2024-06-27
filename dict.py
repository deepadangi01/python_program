#-----typecasting ----->
#this is mutable;
my_dict=dict()
print(my_dict)
print(id(my_dict))
print(type(my_dict))

my_dict['name']="deepa"
print(my_dict)
my_dict['qualification']="Btech"
print(my_dict)
print("lenght of dict ",len(my_dict))
print(max(my_dict))
my_dict['name']="akku"
my_dict['age']=25
print(min(my_dict))
#my_dict[1]
print(max(my_dict))#max and min -- is ascy value base 
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get('roll','guest'))#guest-->default  value 
print(my_dict.pop('age'))



# print(my_dict)
# print(id(my_dict))
# del my_dict['name']
# print(my_dict)
#print(my_dict.clear())


#print(my_dict['name'])


