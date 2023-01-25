# help(list)

list_one = ['Jack Burton', 'Ellen Ripley', 'Korben Dallas']
print('Initial:')
print(list_one)

list_one.append('Leeloo Dallas')
print('Append:')
print(list_one)

list_two = list(list_one)
print('Copy:')
print(list_one)
print(list_two)

print('Index: "Jack Burton"')
print(list_one.index('Jack Burton'))
# Causes an error
# print(list_one.index('leeloo'))

print('Count: "Leeloo Dallas"')
list_one.append('Leeloo Dallas')
print(list_one.count('Leeloo Dallas'))

print('Insert: "list_one.insert(1, \'John Nada\')"')
list_one.insert(1, 'John Nada')
print(list_one)

print('Remove: "list_one.remove(\'John Nada\')"')
list_one.remove('John Nada')
print(list_one)

print('Reverse:')
list_one.reverse()
print(list_one)

print('Sort:')
list_one.sort()
print(list_one)

print('Clear:')
list_one.clear()
print(list_one)