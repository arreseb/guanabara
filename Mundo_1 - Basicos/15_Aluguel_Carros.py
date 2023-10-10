#https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23
#

dias = float(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
preco_dia = 60
preco_km = 0.15

despesa = float((dias * preco_dia) + (km_rodados * preco_km))

print('O total a pagar é de R$ {:.2f}'.format(despesa))
