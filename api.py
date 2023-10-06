import openai

# Substitua "sua_chave_da_openai" pela sua chave de API da OpenAI
openai.api_key = "chave do chatgpt aqui"

def gerar_texto(input_string):
    # Chame a API da OpenAI para gerar texto
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_string,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Retorne o texto gerado
    return resposta.choices[0].text

# Exemplo de uso:
entrada = "Quero gerar um texto sobre programação."
texto_gerado = gerar_texto(entrada)
print(texto_gerado)

