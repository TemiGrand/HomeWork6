#Работа со словорями
my_dict = {'Temir': 2005, 'Artem': 1977, 'Anna': 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Temir'))
print('Not existing value:', my_dict.get('Grisha'))
my_dict.update({'Pavel': 2010, 'Rima': 1994})
a = my_dict.pop('Anna')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

print('\n')

#Работа с множествами
my_set = {3, 34, 3, 4, 'a', 'b', 'c', 'a', True, False, False, True, 0.32, 3.5, 2.6, .32}
print('Set:', my_set)
my_set.update({6, 'Hello!'})
my_set.discard(34)
print('Modified set:', my_set)