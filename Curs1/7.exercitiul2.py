vocale = "aeiouAEIOU"
string = "Salutare, ce mai faci?"

## Varianta 1
def elimina_vocala(ch):
    return ch not in vocale
print("".join(filter(elimina_vocala, string)))

## Varianta 2
print("".join(filter(lambda x: x not in vocale, string)))

## Varianta 3 - Traditional - list comprehention

print("".join([ch for ch in string if ch not in vocale]))
