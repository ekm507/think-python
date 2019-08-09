a = 1
b = 1.0
c = [a]
d = (a, b)
e = dict()
e[1] = 2
f = 'Hi'
print('a', type(a))
print('b', type(b))
print('c', type(c))
print('d', type(d))
print('e', type(e))
print('f', type(f))
g = list()
g.append(a)
g.append(b)
g.append(c)
g.append(d)
g.append(e)
g.append(f)
print('g', g, type(g))
for element in g:
    print(element, type(element))