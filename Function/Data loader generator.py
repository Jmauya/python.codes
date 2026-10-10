lst = [ x for x in range(500) ] # dataset

def data_loader(chunk_size,lst):
    for i in range(0,len(lst),chunk_size):
        yield lst[i:i+chunk_size]


x = data_loader(5,lst)

print(next(x))
print(next(x))

     
