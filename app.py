tipo_imóvel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ")

consumo_mensal = float(input("Digite o seu consumo mensal de água em m³: "))

match tipo_imóvel:
    case "Comercial" | "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")
    case "Apartamento" | "apartamento" if consumo_mensal < 10:
        print("Consumo econômico - excelente controle de água!")
    case "Apartamento" | "apartamento" | "Casa" | "casa" if consumo_mensal <= 25:
        print("Consumo moderado - dentro do padrão residencial.")
    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")