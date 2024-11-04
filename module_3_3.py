def print_params(a = 1, b = 'строка', c = True) :
    return a, b, c

print(print_params())
print(print_params(a=5))
print(print_params(b='jhdbmjhdbj'))
print(print_params(c=5))
print(print_params(b=25))
print(print_params(c=[1,2,3]))

values_list = [456, 'True', True]
values_dict = {'a' : 323, 'b' : 'cvncm', 'c' : False}
print(print_params(*values_list))
print(print_params(**values_dict))

values_list_2 = ['zxvzdfn', True]
print(print_params(*values_list_2, 42))
