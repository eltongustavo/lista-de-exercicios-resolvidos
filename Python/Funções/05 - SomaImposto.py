def SomaImposto(taxa_porcentagem, custo):
    total = custo + (taxa_porcentagem * 100 / custo)
    return total

print(SomaImposto(5, 100))
