# DataCleaner

### Ferramenta de diagnóstico e preparação de dados com Python

<p align="center">
  Projeto voltado à identificação, análise e tratamento de problemas de qualidade em bases de dados nos formatos CSV e Excel (XLSX).
</p>

<p align="center">
  <strong>Status:</strong> Em desenvolvimento
</p>

---

## Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Problema e proposta](#-problema-e-proposta)
- [Objetivos](#-objetivos)
- [Funcionalidades planejadas](#-funcionalidades-planejadas)
- [Tecnologias](#-tecnologias)
- [Arquitetura do projeto](#-arquitetura-do-projeto)
- [Princípios de desenvolvimento](#-princípios-de-desenvolvimento)
- [Etapas do desenvolvimento](#-etapas-do-desenvolvimento)

---

## Sobre o projeto

O **DataCleaner** é um projeto desenvolvido em Python com foco na qualidade, organização e preparação de dados.

A proposta é construir uma ferramenta capaz de receber bases de dados em formatos CSV e XLSX, realizar diagnósticos sobre sua estrutura e identificar possíveis inconsistências que possam comprometer análises posteriores.

A ferramenta também pretende oferecer mecanismos de tratamento e validação, permitindo maior controle sobre as alterações realizadas nos registros.

O projeto está sendo desenvolvido como uma aplicação modular, buscando facilitar a manutenção, a expansão e a reutilização de seus componentes.

## Problema e proposta

Bases de dados utilizadas em processos de análise frequentemente apresentam problemas que precisam ser identificados e tratados antes de sua utilização.

Entre os exemplos estão:

- Valores ausentes ou preenchidos incorretamente.
- Registros duplicados, inclusive duplicidades parciais.
- Datas armazenadas em diferentes formatos.
- Inconsistências em valores numéricos.
- Informações textuais sem padronização.
- Problemas de integridade e consistência dos registros.

O DataCleaner pretende centralizar essas etapas em uma única ferramenta, tornando o processo de preparação dos dados mais organizado, rastreável e confiável.

## Objetivos

O desenvolvimento do projeto busca:

1. Automatizar etapas de diagnóstico e preparação de dados.
2. Identificar diferentes categorias de inconsistências.
3. Desenvolver mecanismos de tratamento específicos para cada tipo de problema.
4. Permitir maior controle sobre as decisões de tratamento.
5. Validar a consistência dos dados após as alterações.
6. Exportar os resultados em formatos adequados para utilização posterior.

## Funcionalidades planejadas

As funcionalidades abaixo representam o escopo previsto para o desenvolvimento:

| Área | Objetivo |
|---|---|
| Diagnóstico | Identificar problemas de qualidade na base de dados. |
| Valores ausentes | Detectar e oferecer alternativas de tratamento. |
| Datas | Identificar e padronizar diferentes formatos de datas. |
| Duplicidades | Identificar registros totalmente ou parcialmente duplicados. |
| Números | Identificar e tratar inconsistências em dados numéricos. |
| Textos | Padronizar informações textuais. |
| Validação | Verificar a consistência dos dados processados. |
| Exportação | Gerar arquivos com os resultados do processamento. |

*As funcionalidades serão implementadas e validadas progressivamente durante o desenvolvimento.*

## Tecnologias

As seguintes tecnologias compõem a base tecnológica do projeto:

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal de desenvolvimento. |
| Pandas | Manipulação, análise e transformação de dados. |
| OpenPyXL | Leitura e escrita de arquivos Excel. |
| Pytest | Testes automatizados e validação dos componentes. |
| Visual Studio Code | Ambiente de desenvolvimento. |

## Arquitetura do projeto

O projeto foi organizado em módulos independentes, buscando separar responsabilidades e facilitar a evolução da aplicação.

```text
DataCleaner/
│
├── data/
│   ├── entrada/
│   └── saida/
│
├── src/
│   ├── unit.py
│   ├── ausente.py
│   ├── datas.py
│   ├── diagnose.py
│   ├── duplicates.py
│   ├── exportação.py
│   ├── importação.py
│   ├── números.py
│   ├── textos.py
│   └── validação.py
│
├── tests/
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Organização dos diretórios

**`data/entrada/`**

Local destinado aos arquivos originais utilizados como entrada do processamento, incluindo bases CSV e XLSX.

**`data/saida/`**

Diretório destinado ao armazenamento dos resultados gerados pela aplicação.

**`src/`**

Contém os módulos responsáveis pelas diferentes etapas de diagnóstico, tratamento, validação e exportação dos dados.

**`tests/`**

Diretório destinado à implementação de testes automatizados para verificar o comportamento e a confiabilidade dos componentes.

### Arquivos principais

- `main.py`: ponto de entrada da aplicação.
- `requirements.txt`: registro das dependências do projeto.
- `.gitignore`: definição dos arquivos e diretórios que não devem ser versionados.
- `README.md`: documentação e apresentação do projeto.

## Princípios de desenvolvimento

Durante a implementação, serão considerados alguns princípios importantes:

- **Modularidade:** separar as responsabilidades em componentes independentes.
- **Integridade:** preservar os arquivos originais utilizados como entrada.
- **Confiabilidade:** validar os resultados após os procedimentos de tratamento.
- **Rastreabilidade:** permitir compreender as alterações realizadas nos registros.
- **Manutenibilidade:** estruturar o código para facilitar futuras modificações e expansões.

## Etapas do desenvolvimento

O projeto seguirá uma evolução progressiva, contemplando:

1. Estruturação do ambiente e arquitetura.
2. Implementação da importação e do diagnóstico dos dados.
3. Desenvolvimento dos módulos de tratamento.
4. Implementação dos mecanismos de validação.
5. Integração dos componentes na aplicação principal.
6. Desenvolvimento e execução dos testes.
7. Implementação da exportação e documentação dos resultados.

---

<p align="center">
  <strong>DataCleaner</strong><br>
  Projeto de desenvolvimento em Python<br>
  Em construção.
</p>