#simple decorator function

# def outerfun(a):
# 	print("Outer function : ",a)

# 	def innerfun(b):
# 		print("Inner function : ",b)
# 	return innerfun

# obj = outerfun(5)

# obj(4)


#decorator function with parameter

# def sum(a,b):
# 	return(a+b)

# def sub(a,b):
# 	return(a-b)

# def main(func):
# 	def cal(a,b):
# 		return(func(a,b))
# 	return cal

# a = main(sum)
# print(a(2,3))

# def function1(func):
# 	def wrapp():
# 		print("Inside Wrapper")
# 		func()
# 		print("smit")
# 	return wrapp

# @function1
# def dis():
# 	print("hello")

# dis()

#decorator with argument

# def function1(func):
# 	def wrapper(*args, **kwargs):
# 		print("Hello wrapper")
# 		func(*args, **kwargs)
# 		print("call to the decorator")
# 	return wrapper

# @function1
# def dis(name1,name2):
# 	print(f"Name1 is : {name1} \nName2 is : {name2}")

# dis("smit","patel")

#class Decorator

class square:

	def __init__(self,length):
		self._length = length

	@property
	def length(self):
		return self._length
	
	# @length.setter
	# def length(self,value):
	# 	if value >= 0:
	# 		self._length = value
	# 	else:
	# 		print("Error")

	@property
	def area(self):
		return(self._length**2)

s = square(5)
print(s.length)
print(s.area)

	