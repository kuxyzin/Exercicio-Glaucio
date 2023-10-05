
maior_altura = 0
menor_altura = float('inf')


soma_altura_homens = 0
num_mulheres = 0


for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    genero = input(f"Digite o gênero da pessoa {i + 1} (H para homem ou M para mulher): ").upper()

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if genero == 'H':
        soma_altura_homens += altura
    elif genero == 'M':
        num_mulheres += 1

media_altura_homens = soma_altura_homens / 15 if soma_altura_homens > 0 else 0

print(f"A maior altura do grupo é: {maior_altura} metros")
print(f"A menor altura do grupo é: {menor_altura} metros")
print(f"A média de altura dos homens é: {media_altura_homens:.2f} metros")
print(f"O número de mulheres no grupo é: {num_mulheres}")
