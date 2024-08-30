#DESAFIO
#EXERCÍCIO 1

def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

total = mult(1, 2, 3, 4, 5)
print(total)
print(1*2*3*4*5)

#EXERCÍCIO 2

def pari(x):
    divisivel = x % 2 == 0
    if divisivel:
        return f'O {x} é PAR'
    # else: neste caso else seria redundante
    return f'O {x} é ÍMPAR'
    
    
print(pari(782))
print(pari(233))
print(pari(672))
print(pari(985))
print(pari(806))






