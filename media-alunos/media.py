#verifica se o valor digitado é um numero válido
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
#verifica se o valor digitado é valido    
def valida_valor(valor):
    if is_float(valor) and float(valor) > 0:
        return True
    else:
        print("Digite um valor válido!")
        return False            

#verifica se o aluno está aprovado, reprovado ou em exame 
def examina_media(media):
    if media >= 7:
        return "aprovado"

    elif media > 4.9 and media < 7:
        return "exame"

    else:
        return "reprovado"
    
soma_notas = 0

for n in range(0,4):
    while True:
        nota = input(f"Digite o valor da nota {n+1}: ")
        if valida_valor(nota):
            soma_notas += float(nota)
            break

media = soma_notas / 4

print(f"Media: {media:.1f}")
resultado = examina_media(media)

if resultado == "aprovado" or resultado == "reprovado":
    print(f"Aluno {resultado}.")
else:
    print("Aluno em exame.")
    while True:
        nota_exame = input("Nota exame: ")
        if valida_valor(nota_exame):
            media_final = (media + float(nota_exame)) / 2
            if media_final > 5:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
                
            print(f"Media Final: {media_final:.1f}")
            break


