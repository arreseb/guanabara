
variavel = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(variavel))
print("Só tem espaços?", variavel.isspace())
print("É um número?", variavel.isnumeric())
print("É alfanumérico?", variavel.isalnum())
print("Está em minúsculas?", variavel.islower())
print("Está em maiúsculas?", variavel.isupper())
print("Está Capitalizada?", variavel.istitle())
