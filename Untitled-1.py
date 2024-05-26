print("Calculo para a soma das nota atuais")
print()
lista =[]
print("Digite a primeira média bimestral: ")
media1 = float(input())
lista.append(media1)

print("Digite a segunda média bimestral: ")
media2 = float(input())
lista.append(media2)

print("Digite a terceira média bimestral: ")
media3 = float(input())
lista.append(media3)

print("Digie a quarta média bimestral: ")
media4 = float(input())
lista.append(media4)

media = (lista[0]+(lista[1]*2)+(lista[2]*2)+(lista[3]*2))
print( "a média seria",media)
if media >= 49:
    print("Parabéns você foi aprovado com a média:",media)
else:
    print("Infelizmente você foi reprovado com a seguinte média: ",media)


#o autor desse codigo é Arthur Ramos Dos Santos,fiz isso com o intuito de ajudar os alunos,pq ja estive na pele de vcs