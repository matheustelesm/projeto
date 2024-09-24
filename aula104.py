from itertools import count

c1 = count(start=2, step=10) # contator infinito não tem fim.
r1 = range(5, 100, 5) # não é um iterator e tem fim.

print("c1", hasattr(c1, '__iter__'))
print("c1", hasattr(c1, '__next__'))
print("r1", hasattr(r1, '__iter__'))
print("r1", hasattr(r1, '__next__'))

print("COUNT")
for i in c1:
    if i >= 100:
        break
    print(i)


print(50*'-')
print("RANGE")
for i in r1:
    print(i)