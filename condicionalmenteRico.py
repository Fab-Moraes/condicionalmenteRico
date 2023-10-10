#  o código está encapsulado em uma função realizar_saque, que torna mais modular e legível, permitindo a entrada de dados uma única vez e chamando a função para realizar o saque e imprimir o resultado.


def realizar_saque(saldo_total, valor_saque):
    if saldo_total >= valor_saque:
        saldo_total -= valor_saque
        return f"Saque realizado com sucesso. Novo saldo: {saldo_total}"
    else:
        return "Saldo insuficiente. Saque nao realizado!"

# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# Chama a função e imprime o resultado
resultado = realizar_saque(saldo_total, valor_saque)
print(resultado)
