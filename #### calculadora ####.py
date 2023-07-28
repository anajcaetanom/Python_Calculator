#### calculadora ####

def adi(n1,n2):
    conta = n1 + n2
    return conta

def subt(n1,n2):
    conta = n1 - n2
    return conta

def multi(n1,n2):
    conta = n1 * n2
    return conta

def divi(n1,n2):
    conta = n1/n2
    return conta

def operacao(n1,n2,op):
    if op == "ad":
        return adi(n1,n2)
            
    elif op == "sub":
        return subt(n1,n2)
        
    elif op == "mult":
        return multi(n1,n2)
        
    elif op == "div":
        return divi(n1,n2)
    
    else: return "Insira uma operação válida."


def main():
    p = "Operações:\nad = adição\nsub = subtração\nmult = multiplicação\ndiv = divisão\n"
    print(p)
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))
    op = str(input("Insira a operação: "))

    resultado = operacao(n1,n2,op)

    while resultado == "Insira uma operação válida.":
        print("\nInsira uma operação válida.\n")
        print(p)
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        op = str(input("Insira a operação: "))

        resultado = operacao(n1,n2,op)

    print (f"\n{resultado}\n")

    resposta = str(input("Continuar a usar a calculadora? Digite 'sim' ou 'nao': "))

    while resposta.lower() == "sim":
        print(p)
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        op = str(input("Insira a operação: "))

        resultado = operacao(n1,n2,op)

        while resultado == "Insira uma operação válida.":
            print(p)
            n1 = float(input("Insira o primeiro número: "))
            n2 = float(input("Insira o segundo número: "))
            op = str(input("Insira a operação: "))

            resultado = operacao(n1,n2,op)

        print (f"\n{resultado}\n")

        resposta = str(input("Continuar a usar a calculadora? Digite 'sim' ou 'nao': "))

if __name__=="__main__":
    main()