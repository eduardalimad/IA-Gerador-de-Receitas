from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def llm_response(prompt, **kwargs):
    max_tokens = kwargs.get('max_tokens', 1500)
    temperature = kwargs.get('temperature', 0)

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role':'user','content':prompt}],
        n=1,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return response.choices[0].message.content

def generate(ingredientes, tipo, culinaria, nivelUsuario, qtdPessoas, restricoes):
    prompt = f'''
        Você é um cozinheiro muito experiente e dá sugestões de receitas.
        1. Faça uma receita que possua os seguintes ingredientes: {ingredientes}. 
        Ela deve ser do {tipo} da culinária {culinaria}. Essa receita terá as seguintes restrições: {restricoes}, e deve servir um total de {qtdPessoas} pessoas. 
        Lembre-se que a pessoa que irá fazer essa receita possui um nível {nivelUsuario} de experiência cozinhando.
        2. Retorne um unico padrão de JSON. Ele deve ter as seguintes propriedades: titulo, ingredientes e modo_preparo com os respectivos valores associados.
        3. Regra: eu quero somente um JSON de resposta, não quero a receita em texto, por favor, me retorne apenas um JSON e sem colocar na sua resposta o valor: 
        ```
            json
            conteúdo json
        ``` 
        quero somente o conteúdo JSON, sem a formatação.
        Não enumerar o modo de preparo, isso será feito no front, apenas separar por topicos
        4. Regra: se o usuário não informar o tipo de culinária, você atribui automaticamente a culinária brasileira
        5. Regra: se o usuário não informar o nível de experiência, você pode deduzir que ele é experiente.
        6. Regra: se o usuário não informar o tempo de preparo, você pode deduzir que ele gostaria de preparar em média em 30 minutos.
        7. Regra: se o usuário não informar as restrições, você pode adicionar todos os 5ingredientes que ele colocou.
        8. Regra: se o usuário colocar um ingrediente inválido, retornar ao usuário que não podemos gerar uma receita com o ingrediente inválido. Exemplo de retorno:
            exemplo de retorno 
            "error": true,
            "mensagem": "A entrada fornecida violou o sistema" (aqui você diz o motivo pelo qual não é possível gerar essa receita).
        '''
    print(llm_response(prompt))
    return llm_response(prompt)
    
# ingredients = (input('Quais ingredientes você tem disponíveis em casa?'))
# tipo = (input('Qual tipo de refeição você deseja ? (Ex: café da manhã, almoço, jantar, ou lanche)'))
# culinaria = (input('Qual tipo de culinaria você deseja na sua receita ? (ex:italiana, japonesa, mexicana, etc.)'))
# tempoPreparo = (input('Qual tempo esperado você quer levar nessa receita ?'))
# nivelUsuario = (input('Você possui experiência cozinhando ?'))
# qtdPessoas = (input('Essa refeição é pra quantas pessoas ?'))
# restricoes= (input('Você possui alguma restrição ? (ex: "sem glúten", "vegetariano", ou "baixa caloria".)'))