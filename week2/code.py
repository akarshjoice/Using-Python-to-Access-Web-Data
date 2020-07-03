import re

handle=open('test.txt')
lis=[]
sum=0
for lin in handle:
	line=lin.rstrip()
	p=line.split()
	for i in p:
			li=re.findall('[0-9]+',i)
			if len(li) > 0:
					for i in li:
						sum+=int(i)
print(sum)
                     