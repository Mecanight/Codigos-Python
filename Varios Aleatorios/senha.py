def valida_senha():
    lista_numeros = "0123456789"
    lista_caracteres_especiais = "!@#"

    senha_digitada = str(input("Digite sua senha.: "))

    tem_numero = False
    tem_caracter_especial = False

    print(senha_digitada)

    for caractere in senha_digitada:
        if caractere in lista_numeros:
            tem_numero = True
            break
        else:
            tem_numero = False

    for caractere in senha_digitada:
        if caractere in lista_caracteres_especiais:
            tem_caracter_especial = True
            break
        else:
            tem_caracter_especial = False
    
    if tem_caracter_especial == True and tem_numero == True:
        print("Senha Válida")
    else:
        print("Senha Inválida")

if __name__ == "__main__":
    valida_senha()