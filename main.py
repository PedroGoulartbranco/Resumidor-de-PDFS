from codigo import *


while True:
    resumir_mais_true_false= True
    print("-=" * 30)
    print("Resumidor de PDFs")
    print("-=" * 30)
    caminho_pdf = input("Digite o caminho ou arraste o arquivo do pdf: ")
    limpar_terminal()
    texto = pdf_extrair_texto(caminho_pdf)
    while texto == False:
        print("-=" * 30)
        caminho_pdf = input("Digite o caminho ou arraste o arquivo do pdf: ")
        limpar_terminal()
        texto = pdf_extrair_texto(caminho_pdf)
    print("-=" * 30)
    prompt = tipo_resumo()
    limpar_terminal()
    print("-=" * 30)
    texto_resumido = resumir_pdf(texto, prompt)
    print(texto_resumido)
    while resumir_mais_true_false:
        print("-=" * 30)
        resumir_mais_true_false = pergunta_resumir_mais()
        if resumir_mais_true_false:
            texto_resumido = resumir_mais(texto_resumido)
            print("-=" * 30)
            print(texto_resumido)
    print("-=" * 30)
    print("[0] Mais resumos\n[1] Sair")
    print("-=" * 30)
    continuar = int(input("Digite sua opção: "))
    if continuar == 1:
        break
    limpar_terminal()