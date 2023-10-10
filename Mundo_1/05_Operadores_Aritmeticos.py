n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

s = n1+n2    #soma
su = n1-n2   #subtração
m = n1*n2    #multiplicação
d = n1/n2    #divisão
di = n1//n2  #parte inteira da divisão
dr = n1%n2   #resto da divisão
e = n1**n2   #exponenciação

#saída

print("A soma é igual a: {}. a subtração {}, o produto {}, a divisão {:.2f}, a parte inteira da divisão {}, o resto da divisão {} e a potênciação {}".format(s, su, m, d, di, dr, e))
