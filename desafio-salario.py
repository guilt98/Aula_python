

def salario_hora (horas_trabalhadas,valor_hora):
    salario_pago = (horas_trabalhadas*valor_hora)

    return (salario_pago)


horas_trabalhadas = int(input("Digite as horas trabalhadas:"))
valor_hora = int(input("Digite o valor das horas:"))

print (" ")

salario_final_mes = salario_hora(horas_trabalhadas,valor_hora)

print("O valor a pagar no final do mes é:",salario_final_mes)
                        
