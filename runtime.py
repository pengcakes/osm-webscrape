import time

start = time.time()


#print('hello world')

test_list=['a', 'b', 'c']
empty_list=[]


test_list.append(empty_list)

print(test_list)




end = time.time()
print(round(end - start, 5))