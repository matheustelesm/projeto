# Introdução ás Generator fuctions em Python
# Generator = (n for n in range(10000))

# def generator(n=0):
#     yield 1 # pausa a execução # toda função que tem o yield é uma generator fuction
#     print('Continuando...')
#     yield 2 # pause
#     print('MAIS UMA VEZ...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'

# def generator(n=0, maximum=10):
#     while True:
#         yield n 
#         n += 1

#         if n >= maximum:
#             return


# gen = generator(maximum=10000)

# for n in gen:
#     print(n)


# yield from

def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

def gen3():
    yield from gen2()
    yield 7
    yield 8
    yield 9


g1 = gen2
for i in g1:
    print(i)
