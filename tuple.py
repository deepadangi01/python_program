my_tuple=(56,99,12,4,2,7)
b=(5,6,7,8)
v=list(b)
a=[1,2,3,4,5]
print(my_tuple)
print("-------in-build function-------")
print(min(my_tuple))
print(max(my_tuple))
print(len(my_tuple))
print(sum(my_tuple))
t=list(my_tuple)
t.append(a)
t.append(v)

print(tuple(t))

print("-------in-build method-------")
print(my_tuple.count(99))
print(my_tuple.index(12))