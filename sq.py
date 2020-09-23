import queue

q = queue.Queue(maxsize=10)

for i in range(1,11):
	q.put(i)

for i in range(0,10):
	print(q.get())

# x = ['hello']

# x.append('smit')
# x.append('patel')

# print(x)

# print(x.pop())
# print(x)