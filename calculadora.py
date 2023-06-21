n = 9
m = 5


def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def is_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print('soma: ', soma(n,m))
print('subtração: ', subtracao(n,m))
print('multiplicação: ', multiplicacao(n,m))

print('divisão:', divisao(n,m))
print('o numero ', n, 'é par:', is_par,(n))