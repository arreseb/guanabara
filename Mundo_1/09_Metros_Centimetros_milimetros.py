##Desafio 8: Escreva um programa que leia um valor em metros e o
# exiba convertido em centimetros e milimetros:

m = float(input('Digite a metragem: '))
print("A medida de {}m, equivale a: {:.3f}km; {:.2f}hm, {:.1f}dam, {:.2f}dm, {:.2f}cm, {:.2f}mm ".format
      (m, (m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))