dano = float(input("Quanto de dano você recebeu? "))
defesa = float(input("Quanto de defesa você tem? "))

dano_real = dano - defesa

if dano_real == 0:
    dano_real = 0

print(f"O dano real sofrido foi: {dano_real}")