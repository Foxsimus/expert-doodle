
#изменить значение первого элемента
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print()
#Присоединение элементов в конец списка
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ktm')
print(motorcycles)
print()
#в пустой список добавляются элементы
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print()
#Метод insert() позволяет добавить новый элемент в произвольную позицию списка.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print()
#Удаление элемента с использованием команды del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print()
#Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print()
#Извлечение элементов из произвольной позиции списка
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print()
#Удаление элементов по значению remove единыжды
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print()
#remove() также может использоваться для работы со значением, которое удаляется из списка
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
