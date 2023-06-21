import numpy as np

numeros = ([1,2,3,4,5,6])
def is_par(numeros):
    if numeros % 2 == 0:
        return True
    else:
        return False


def soma_de_pares(numeros):
  par_list = []
  for item in numeros:
      if is_par(item):
          par_list.append(item)
  return np.sum(par_list)

frase = 'hoje é dia dos namorados'
def string(frase):
   frase2 = ''
   vogais = ['a','e','i','o','u']
   for caractere in frase:
       if caractere in vogais:
           frase2 += caractere.upper()
       else:
            frase2 += caractere

   return(frase2)














