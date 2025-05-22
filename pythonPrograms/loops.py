l = [1,2,3,4,5]

# for i in list:
#     print(i)

itr1 = l.__iter__()
print(f"itr1 : {itr1}") # <class 'list_iterator'> point to the start address of the list

itr = iter(l)
print(f"itr : {itr}")            # <class 'list_iterator'> point to the start address of the list
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
# print(itr.__next__()) # StopIteration exception (It is handled by the for loop or other iterators)
print(itr)


print("Comparision for file")

f = open("test.txt")

print(iter(f) is f)
print(f.__iter__() is f)
print(iter(f) is f.__iter__())

print("Comparision for list")

print(iter(l) is l)
print(l.__iter__() is l)
print(iter(l) is l.__iter__())