import random
import enum

class Optiuni(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizard = 4
    Spock = 5

    def __str__(self):
        return self.name
    
    
print([op.value  for op in Optiuni])


# print(Optiuni.Rock)
# print(Optiuni.Rock.value)


while True:
    client = input('Introduceti o valoare 1. Rock, 2. Paper, 3. Scissors\n')

    server = random.choice([1, 2, 3])
    print(server)
    server = Optiuni(server)

    try:
        client = int(client)
        client = Optiuni(client)
    except:
        print('Valoare incorecta')

    if client == server:
        print('Egalitate')
    elif client == Optiuni.Rock and server == Optiuni.Scissors:
        print('Ai castigat !')
    elif client == Optiuni.Scissors and server == Optiuni.Paper:
        print('Ai castigat !')
    elif client == Optiuni.Paper and server == Optiuni.Rock:
        print('Ai castigat !')
    else:
        print('Ai pierdut !')
    print('Client :', client, 'Server :', server)
     
