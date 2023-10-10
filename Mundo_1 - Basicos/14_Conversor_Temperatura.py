#https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=22
#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = ((9*celsius)/5) + 32

print('A temperatura de {:.2f}ºC, corresponde a {:.2f}ºF'.format(celsius, fahrenheit))
