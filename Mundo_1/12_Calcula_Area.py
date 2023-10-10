#Desafio 11: Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = float(largura*altura)
litros = float(area / 2)

print('Sua parede tem a dimensão de {} x {} e sua área é de: {}m2.'.format(largura, altura, area))
print('Para pintar esta parede, você precisará de {:.2f}l de tinta'.format(litros))