# Criar um sistema que criptografe uma palavra de acordo com a posição dela no alfabeto

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

frase = str(input("Informe a frase que deseja criptografar: ")).lower()

frase_criptografada = []

for i in range(len(frase)):
    cadaLetra = frase[i]

    frase_criptografada.append(alfabeto.index(cadaLetra) + 1)


print()
print("A palavra criptografada foi criada: ")


for i in range(len(frase_criptografada)):
    print(frase_criptografada[i], end = " ")
    