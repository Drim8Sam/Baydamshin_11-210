quantity = int(input())
lines = []
for i in range(quantity):
    q = input()
    lines.append(q)

for i in lines:
    i = i.strip('0')
    print(i.count('0'))
    
