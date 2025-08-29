from codigo import *


while True:
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
        print(resumir_pdf_pequeno(texto, prompt))
    print("-=" * 30)
    print("[0] Continuar\n[1] Sair")
    continuar = int(input("Digite sua opção: "))
    if continuar == 1:
        break
    limpar_terminal()