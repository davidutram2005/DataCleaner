# importar Excel e CSV.

import pandas as pd  #le os arquivos e transforma em DataFrame
from pathlib import Path #importa o Path do pathlib para manipular os caminhos dos arquivos


def importar_arquivo(caminho_arquivo):
    """
        Função usada para importar arquivos CSV e EXCEL, retornando como um DataFrame
    """

    #converte o caminho do arquivo para um Path, caso seja passado como string
    caminho_arquivo = Path(caminho_arquivo)

    #verifica se o caminho existe, levantando um erro
    if not caminho_arquivo.exists():
        raise FileNotFoundError(
            #FileNotFoundError é uma exceção que aparece quando o arquivo nao é encontrado
            f"Arquivo {caminho_arquivo} não encontrado no caminho especificado. " 
        )

    #verifica o arquivo, levanta um erro se nao for CSV ou EXCEL
    extensao = caminho_arquivo.suffix.lower()
    try: 
        if extensao == ".csv":
            return pd.read_csv(caminho_arquivo, sep=";")
        #pd.read_csv é uma função do pandas que lê arquivos CSV e retorna um DataFrame
    
        elif extensao == ".xlsx":
            return pd.read_excel(caminho_arquivo)

        else:
            raise ValueError(
                f"O arquivo {caminho_arquivo} não é CSV nem EXCEL."
                "Forneça um arquivo válido com a extensão .csv ou .xlsx."
            )
        #raise é usado para levantar uma exceção, nesse caso ValueError, que é uma exceção que aparece quando o valor passado para uma função não é válido

    
    #(pd.errors.ParserError, OSError, ValueError) as erro: 
    #é usado para capturar erros que podem ocorrer na leitura do arquivo:
    #ParserError (erro de parsing),
    #OSError (erro de sistema operacional) e 
    #ValueError (erro de valor). 
    except (pd.errors.ParserError, OSError, ValueError) as erro: 
        raise RuntimeError(
            f"Erro ao ler o arquivo {caminho_arquivo}: o erro foi {erro}"
        ) from erro 

