test_string = 'James is good in Science , Science is James favourite subject. '
print("The original string is : " + str(test_string))
repl_dict = {'James' :  'his', 'Science' : 'it' }
test_list = test_string.split(' ')
res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != index 
                                   else val for index, val in enumerate(test_list)])
print("The string after replacing : " + str(res))
