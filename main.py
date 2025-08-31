from codigo import *


while True:
    resumir_mais_true_false= True
    print("-=" * 30)
    print("Resumidor de PDFs")
    print("-=" * 30)
    print("[0] PDF pequeno\n[1] PDF grande")
    print("-=" * 30)
    resposta = int(input("Digite sua opção: "))
    limpar_terminal()
    if resposta == 0:
        texto = pdf_pequeno("baleia.pdf")
        print("-=" * 30)
        prompt = tipo_resumo()
        limpar_terminal()
        print("-=" * 30)
        texto_resumido = resumir_pdf_pequeno(texto, prompt)
        print(texto_resumido)
    while resumir_mais_true_false:
        print("-=" * 30)
        resumir_mais_true_false = pergunta_resumir_mais()
        if resumir_mais_true_false:
            texto_resumido = resumir_mais(texto_resumido)
            print(texto_resumido)
    print("-=" * 30)
    print("[0] Mais resumos\n[1] Sair")
    print("-=" * 30)
    continuar = int(input("Digite sua opção: "))
    if continuar == 1:
        break
    limpar_terminal()