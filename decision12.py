
#Дана строка, которая может содержать или не содержать письмо о заинтересованности. Распечатать указатель
#место первого и последнего появления ф. Если буква f встречается только один раз,
#затем выведите его индекс. Если буква f не встречается, то ничего не печатать.
#Не используйте петли в этой задаче.

string = str(input("Enter: "))
if string.count('f') == 1:
    print(string.index('f'))
elif string.count('f') > 1:
    print(string.index('f'), string.index('f',))
else:
    print()        


