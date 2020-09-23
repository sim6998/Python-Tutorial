import csv
import pandas

file = open("sample.txt","r+")

# print(csv.__file__)

# l = csv.reader(file,delimiter=',')
# line_count=0

# for i in l:
# 	if line_count == 0:
# 		print(f'Column Names are {",".join(i)}')
# 		line_count += 1

# dic = csv.DictReader(file)

# for row in dic:
# 	if line_count == 0:
# 		print(f'Columns Name : {",".join(row)}')
# 		line_count += 1
# 	print(f'{row["Name"]} is in {row["Department"]} Departmenrt and born in {row["Bod"]}')
# 	line_count += 1
# print(f'Total line {line_count} prepared')

# l = pandas.read_csv(file)
# print(l)


#--------writing-------#

# writer = csv.writer(file,delimiter=",",quotechar='"')

# writer.writerow(['xyz','IT','08-04-1998'])

# l = pandas.read_csv(file)
# print(l)

fieldname = ['Name','Department','Bod']
writer = csv.DictWriter(file,fieldnames = fieldname)

writer.writeheader()
writer.writerow({'Name':'yzx','Department':'che','Bod':'12-10-1995'})

l = pandas.read_csv(file)
print(l)
