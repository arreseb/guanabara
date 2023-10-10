##Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar
# US$ 1,00 = R$ 3,27

reais = float(input('Quantos reais vc tem na carteira: '))
cotacao = 3.27

dolares = float(reais / cotacao)

print('Com R$ {:.2f}, você poderá comprar US$ {:.2f}.'.format(reais, dolares))