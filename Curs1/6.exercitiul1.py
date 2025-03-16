

lista = [10, 2, 30, 50, 300, 10]


## Varianta 1 - filter + functia lambda
print("noua_lista =", list(filter(lambda x : x > 5, lista)))


## Varianta 2 - filter + functie
def elimina_elemente(x):
    return x > 5

print(list(filter(elimina_elemente, lista)))

## Varianta 3 - list comprehention
print([x for x in lista if x > 5])
