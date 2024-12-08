num_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(num_alunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))

    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

media_geral = soma_medias / num_alunos

print(f"\nA média geral da turma é: {media_geral:.2f}")