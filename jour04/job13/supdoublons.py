l = [10,20,30,20,10,50,60,40,80,50,40]
print(l)
def enum(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

my_finallist = [i for j, i in enum(l) if i not in l[:j]] 
print(my_finallist)
