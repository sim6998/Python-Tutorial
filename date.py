import time

#returns the total number of ticks spent since 12 AM, 1st January 1970.
print(time.time())

#used get the current time tuple.
print(time.localtime(time.time()))

#time in well formate

print(time.asctime(time.localtime(time.time())))

#used to stop the execution of the script for a given amount of time.
for i in range(0,5):
	print(i)
	time.sleep(1)
