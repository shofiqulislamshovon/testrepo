d={'Name': "Shovon",'id':1005,'age':26,'Varsity':'SMUCT'}
"""print(d)
#get()
print(d.get("wife",'Tabbia'))
print(d)
#setdefault()
print(d.setdefault("wife","Tabbia"))
print(d)     
#for
for x in d:
	print(x)
#forkey_value
for keys in d:
	print(keys,d[keys])	
#1234567
d={}
for value in range(1,11):
	d[value]=value*value
print(d)
#keys values items function	it will returns list
print(d.keys())
print(d.values())
print(d.items())
#printing tuples 
for t in d.items():
	print(t)   
l1=[1,2,3,4,5]
l2=[1,4,9,16,25]
d=dict(zip(l1,l2))
print(d)
l=[1,2,34,5]
d=dict.fromkeys(l,0)
print(d)
d1={1:1,2:4,3:9,4:16}
d2={5:15}
d1.update(d2)
print(d1)"""
d1={1:1,2:4,3:9,4:16}
r=d1.popitem()
print(d1,r)

