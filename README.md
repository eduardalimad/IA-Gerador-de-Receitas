
# IA de receitas ✨

Este projeto é um gerador de receitas que utiliza a API do OpenAI para criar receitas de maneira inteligente. A interface é feita utilizando Streamlit, uma biblioteca Python para construção de dashboards interativos.



## Requisitos

- Python 3.8 ou superior
- Conta e API Key do OpenAI
- Pacotes Python especificados no requirements.txt

## Funcionalidades
- Gera receitas de forma automática com base em sugestões fornecidas pelo usuário.
- Interface interativa usando Streamlit para facilitar o uso.


## Rodando Localmente:
#### Clonando o repositório

```
git clone <URL-do-repositório>
cd <nome-do-diretório>
```

### Crie um ambiente virtual:

```
python -m venv amb
source amb/bin/activate   # Para Linux/Mac
amb\Scripts\activate      # Para Windows

```

### Instale as dependências:

```
pip install -r requirements.txt

```
### Rode o comando:
Dentro da pasta \receitas\script, utilize o seguinte comando:

```
 
 streamlit run streamlit.py

```



## Configure a chave de API do OpenAI:

- Crie um arquivo .env na raiz do projeto.

- Adicione a sua chave de API no arquivo .env: