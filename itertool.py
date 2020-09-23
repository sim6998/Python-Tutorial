import itertools

# a = [1,2,3]
# b = ['a','b','c']

# c = zip(a,b)

# print(type(c))
# print(c)
# print(list(c))

# for i in itertools.count(10,5):
# 	if i==50:
# 		print(i)
# 		break
# 	else:
# 		print(i,end=",")


# count = 1
# for i in itertools.cycle("123"):
# 	if count == 7:
# 		break
# 	else:
# 		print(i)
# 		count += 1


# l = list(itertools.repeat(15,4))
# print(l)

l = list(itertools.product([1,2,6,9],repeat=2))
count = 0
n = 0
print(l)
for i in range(len(l)):
	n = sum(l[i])
	if n == 8:
		count += 1
	else:
		continue

if count == 0:
	print("False")
else:
	print("True")