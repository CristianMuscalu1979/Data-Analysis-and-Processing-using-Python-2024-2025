from functools import reduce

lista = [10, 2, 30, 50, 300, 10]

## Varianta 1 - functia reduce
print(reduce(lambda x, y: x + y, lista)/len(lista))

## Varianta 2 - clasic
print(sum(lista)/len(lista))

## Versiunea 3
print(reduce(lambda x, y: x + y, lista)/reduce(lambda x, y : x + y, map(lambda x:1, lista)))