precos_em_moedas= [
    [10, 12, 15],
    [20, 22, 26],
    [30, 32, 38]
]
taxa_conversao = {
    "BRL": 0.038,
    "IENE": 26.24

}

def conversao_para_iene(preco, moeda):
    return preco * taxa_conversao[moeda]

preco_em_ienes = [
    [conversao_para_iene(preco, "BRL") for preco in linha] if i== 0 
    else [conversao_para_iene(preco, "IENE") for preco in linha]
    for i, linhain enumerate (precos_em_moedas) 
  ]

print("Preços convertidos em ienes:")
for linha in preco_em_ienes
