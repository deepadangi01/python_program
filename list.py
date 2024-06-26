# mylist=[10,30,'asd34','abc','abc',10]
# print(mylist)
# print(mylist[2])
# print(mylist[1])
# print(mylist.index('abc'))
# print(mylist[-1])
# print(mylist[2:])

# mylist[3]="deepa"
# print(mylist)

#----------------------------------------

#------In-build function-----------#

my_list=[50,39,20,10,50,99]
my_list2=['av',45]
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))


#------------In-build Method---------
my_list.append(88)
print(my_list)
# my_list.extend(my_list2)
# print(my_list)

my_list.pop()
print(my_list)
my_list.remove(99)
print(my_list)

my_list.insert(2,66)
print(my_list)

my_list.sort(reverse=True)
print(my_list)

