my_dict = { 'Nune': 1996, 'Paruyr': 1988, 'Artur':2024}
print(my_dict)
print(my_dict['Nune'])
print(my_dict.get('Armine', 'No'))
my_dict.update({'Armine': 1965, 'Artur Big':1961})
print(my_dict.pop('Nune'))
print(my_dict)
print()
my_set = { 12, 15, 34, 12, True, False, False}
print(my_set)
my_set.add(56)
my_set.add('Something')
my_set.remove(12)
print(my_set)