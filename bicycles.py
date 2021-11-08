#перечисление элементов списка в квадратных скобках
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#название первого велосипеда в списке bicycles выводится следующим образом
print(bicycles[0])
#отформатировать при помощи метода title
print(bicycles[0].title())
#выводится второй и четвертый элементы списка
print(bicycles[1])
print(bicycles[3])
#обращения к последнему элементу списка. Индекс –2 возвращает второй элемент от конца списка, индекс –3 — третий элемент от конца и т. д.
print(bicycles[-1])
#создается простое предложение с упоминанием первого велосипеда из списка
message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)
