from televisao import Televisao

# 1. Criar pelo menos três televisores e guardá-los em uma lista
tvs = [
    Televisao("Samsung", 43),
    Televisao("LG", 50),
    Televisao("Philco", 32)
]

# 2. Ligar alguns e deixar pelo menos um desligado diretamente
tvs[0].ligada = True
tvs[1].ligada = True
# tvs[2] continua desligada (False)

# 3. Alterar canal e volume de televisores diferentes diretamente
tvs[0].canal = 5
tvs[0].volume = 25

tvs[1].canal = 12
tvs[1].volume = 70

# 4. Percorrer a lista com for e imprimir os dados
for tv in tvs:
    if tv.ligada:
        print(f"{tv.marca} {tv.polegadas}\" | Ligada | Canal {tv.canal} | Volume {tv.volume}")
    else:
        print(f"{tv.marca} {tv.polegadas}\" | Desligada")

# 5. Mostrar estatísticas ao final (Campeão da quadra para maior TV)
ligados_count = 0
maior_tv = None
soma_polegadas = 0

for tv in tvs:
    soma_polegadas += tv.polegadas
    if tv.ligada:
        ligados_count += 1
    
    # Lógica do "campeão da quadra"
    if maior_tv is None or tv.polegadas > maior_tv.polegadas:
        maior_tv = tv

media_polegadas = soma_polegadas / len(tvs)

print(f"\nTelevisores ligados: {ligados_count}")
if maior_tv is not None:
    print(f"Maior televisor: {maior_tv.marca} {maior_tv.polegadas}\"")
print(f"Média de polegadas: {media_polegadas:.2f}")
