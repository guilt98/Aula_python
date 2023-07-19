#Exemplo 3 - funçoes
#Vamos criar uma funções que recebera 3 notas e calculara a media

def media_aluno (nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3


    return (media)



#recebendo as notas pelo usuario
n1 = float(input("Digite a nota:"))
n2 = float(input("Digite a nota:"))
n3 = float(input("Digite a nota:"))


print(" ")

media_final = media_aluno(n1,n2,n3)

print("A media final do aluno é:",media_final)
