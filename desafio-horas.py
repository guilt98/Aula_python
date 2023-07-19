def salario_hora (salario_mes,dias,horas_trabalhadas):
    salario_pago = ((salario_mes / dias) / horas_trabalhadas)

    return (salario_pago)


salario_mes = int(input("Digite seu salario do mes:"))
dias = int(input("Digite a quantidades de dias no mes:"))
horas_trabalhadas = int(input("Digite as horas trabalhadas:"))


print (" ")

valor_hora = salario_hora(salario_mes,dias,horas_trabalhadas)

print("O valor recebido por hora trabalhada é:",valor_hora)
                        
