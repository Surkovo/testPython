#This program says hi
import sys 

print(sys.version)
print(sys.executable)


name = 'eric Johnson   '
print(name.title().rstrip() + ', once said "like to learn to some Python today?"')

#lists
names = ['kyle', 'doug','cayla','ebi']
print(names[0] + ' you invited to dinner')
print(names[1] + ' you invited to dinner')
print(names[2] + ' you invited to dinner')
print(names[3] + ' you invited to dinner\n')

names[2] = 'ryan'
print(names[0] + ' you invited to dinner')
print(names[1] + ' you invited to dinner')
print(names[2] + ' you invited to dinner')
print(names[3] + ' you invited to dinner\n')

names.insert(0,'Conor')
names.insert(2,'Ivan')
names.append('Gregory')
print(names[0] + ' you invited to dinner')
print(names[1] + ' you invited to dinner')
print(names[2] + ' you invited to dinner')
print(names[3] + ' you invited to dinner')
print(names[4] + ' you invited to dinner')
print(names[5] + ' you invited to dinner')
print(names[6] + ' you invited to dinner\n')

print('sorry' + names.pop() + 'you have been uninvites')
print('sorry' + names.pop() + 'you have been uninvites')
print('sorry' + names.pop() + 'you have been uninvites')
print('sorry' + names.pop() + 'you have been uninvites')
print('sorry' + names.pop() + 'you have been uninvites\n')

print(names)

places = ['japan', 'germany','taiwan','peru','france']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.sort()
print(places)
print(len(places))
for place in places:
    print(place + ' is cool')
print("I haven't visited any of these places")

pizzas = ['cheese','pepporni', 'combo']

for pizza in pizzas: 
    print('I like ' + pizza + ' pizza')
print('Pizza is a good thing')

for value in range(1,21):
    print(value)
million = range(1,1000001)
print(min(million))
print(max(million))
# for x in million:
#     print(x)
print(sum(million))
#odd
odd = range(1,21,2)
for x in odd:
    print(x)
#multiple of 3

threeish = range(3,31,3)
for x  in threeish:
    print(x)
#making list of cubes
cubes = []
for value in range(1,11):
    square = value**2
    cubes.append(square)
    print(square)

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)