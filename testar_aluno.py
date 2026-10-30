from aluno import Aluno

alunos = []

# 1. Ler vários alunos até que o nome digitado seja vazio
while True:
    nome = input("Digite o nome do aluno (ou deixe vazio para sair): ").strip()
    if not nome:
        break
    matricula = input(f"Digite a matrícula de {nome}: ").strip()
    
    novo_aluno = Aluno(nome, matricula)
    alunos.append(novo_aluno)

# Garante que temos dados para testar os requisitos caso o usuário insira os alunos do exemplo
if len(alunos) >= 3:
    # 2. Atribuir notas e faltas diretamente (deixando pelo menos um sem notas)
    alunos[0].notas.append(8.5)
    alunos[0].notas.append(7.0)
    alunos[0].faltas += 2

    alunos[1].notas.append(5.5)
    alunos[1].faltas += 6
    
    # alunos[2] fica sem notas e com 0 faltas

print("\n--- Listagem de Alunos ---")

# 3. Percorrer a lista e mostrar os dados de cada um
for aluno in alunos:
    print(f"{aluno.nome} ({aluno.matricula})")
    print(f"Notas: {aluno.notas}")
    print(f"Faltas: {aluno.faltas}")
    
    # Tratamento para aluno sem notas usando sum() e len()
    if len(aluno.notas) > 0:
        media = sum(aluno.notas) / len(aluno.notas)
        print(f"Média: {media:.2f}")
    else:
        print("Média: sem notas")
    print("-" * 30)

# 4. Mostrar qual aluno tem mais faltas (Campeão da quadra)
aluno_mais_faltas = None

for aluno in alunos:
    if aluno_mais_faltas is None or aluno.faltas > aluno_mais_faltas.faltas:
        aluno_mais_faltas = aluno

if aluno_mais_faltas is not None:
    print(f"Mais faltas: {aluno_mais_faltas.nome} ({aluno_mais_faltas.faltas})")
