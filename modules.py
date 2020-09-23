import random
import statistics

# for i in range(0,10):
# 	a = random.randint(10,20)
# 	print(a)

# print(random.choice([1,2,3,4,5]))
# print(random.randrange(100,200))

l = [10,20,30,40,500,10]

men = statistics.mean(l)
med = statistics.median(l)
mod = statistics.mode(l)
sd = statistics.stdev(l)

print("Mean:",men)
print("Median:",med)
print("Mode:",mod)
print("Standard Deviation:",sd)