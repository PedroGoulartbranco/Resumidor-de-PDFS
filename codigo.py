import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()

chave_api = os.getenv('CHAVE_API')

genai.configure(api_key=chave_api)
modelo_gemini = genai.GenerativeModel("gemini-2.5-flash")

import pdfplumber

caminho_pdf = 'baleia.pdf'

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pdf_extrair_texto(caminho):
    texto = ""
    try:
        with pdfplumber.open(caminho) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text()
        return texto
    except FileNotFoundError:
        print("PDF não encontrado, digite novamento o caminho ou arraste o arquivo.")
        return False
    except:
        print("Erro, tente novamente!")
        return False

def resumir_pdf(texto, prompt_cliente):
    prompt_completo = prompt_cliente + texto
    resposta = modelo_gemini.generate_content(
        contents= prompt_completo
    )
    return resposta.text

def pergunta_resumir_mais():
    print("[0] Resumir mais\n[1] Continuar")
    print("-=" * 30)
    resposta = int(input("Digite sua opção: "))
    if resposta == 0:
        return True
    else:
        return False

def resumir_mais(texto):
    resposta = modelo_gemini.generate_content(
        contents= "Resuma mais esse texto (quando a linha estiver muito grande quebre ela, sem deixar linhas vazias): " + texto
    )
    return resposta.text

def tipo_resumo():
    print(" " * 23  + " MENU RESUMO")
    print("-=" * 30)
    print("[0] Resumo normal\n[1] Resumo Curto\n[2] Resumo Super curto\n[3] Resumo mais tópicos importantes")
    print("-=" * 30)
    numero_resumo = int(input("Digite sua opção:"))
    if numero_resumo == 0:
        prompt = "Faça um resumo normal do seguinte texto (Quando ver que a linha ficou muito grande quebre ela): "
    elif numero_resumo == 1:
        prompt = "Faça um resumo curto desse, mais resumido que o normal do seguinte texto (Quando ver que a linha ficou muito grande quebre ela): "
    elif numero_resumo == 2:
        prompt = "Faça um resumo super curto desse texto tentando resumir ele ao máximo (Quando ver que a linha ficou muito grande quebre ela): "
    elif numero_resumo == 3:
        prompt = "Faça um resumo curto e mais 3 tópicos importantes do seguinte texto (Quando ver que a linha ficou muito grande quebre ela): "
    return prompt