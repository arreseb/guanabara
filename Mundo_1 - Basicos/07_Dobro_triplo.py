##Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2) #raiz = pow(n, (1/2))

#import math
#raiz = math.sqrt(n)



print("O número digitado foi: {}, o seu dobro é igual a: {}, seu triplo {}, e a raiz quadrado do número digitado é igual a {:.2f}".format(n, dobro, triplo, raiz))
