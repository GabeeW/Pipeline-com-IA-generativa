import pandas as pd
import json
import os
from openai import OpenAI


client = OpenAI()

df = pd.read_csv('SDW2023.csv')


user_ids = df['id'].tolist() 

print(user_ids) 


users = df.to_dict(orient='records')


for user in users:

    user['news'] = []


users_valido = [user for user in users if user is not None]
print(json.dumps(users_valido, indent=2))

def generate_ai_news(user):
    response = client.responses.create(
        model="gpt-4.1-mini",  
        input=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )

    return response.output_text.strip()

for user in users:
    news = generate_ai_news(user)
    user["news"].append(news)
    print(f"{user['name']}: {news}")
