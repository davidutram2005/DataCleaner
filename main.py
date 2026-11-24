#no arquivo main.py ; voce vai no arquivo importacao.py e importa a funcao criada (importar_arquivo)
from src.importacao import importar_arquivo
from pathlib import Path #importa o Path do pathlib para manipular os caminhos dos arquivos

#faz a importacao do arquivo, verificando a extensao do arquivo e chamando a funcao importar_arquivo

# caminho_arquivo = Path("data/Entrada/base_grande.csv")
caminho_arquivo = Path("data/Entrada/base_grande.xlsx")

extensao = caminho_arquivo.suffix.lower()

if extensao == ".csv":
    df = importar_arquivo(caminho_arquivo)

elif extensao == ".xlsx":
    df = importar_arquivo(caminho_arquivo)

else: 
    raise ValueError(
        "Erro de importação do arquivo." "Extensão não suportada."
        "Ele nao é EXCEL nem CSV. Forneça um arquivo válido."
    )


print(df.head(10)) #exibe as primeiras 10 linhas do DataFrame importado 

print(df.tail(10)) #exibe as ultimas 10 linhas do DataFrame importado

print(df.shape) #exibe o numero de linhas e colunas do DataFrame importado