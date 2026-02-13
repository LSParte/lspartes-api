import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recommendations(profile_data):

    prompt = f"""
    Com base neste perfil:
    {profile_data}

    Gere:
    - Estilos recomendados
    - Cores ideais
    - Peças de roupa indicadas
    - Style Score (0-10)

    Responda em JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é especialista em moda e análise corporal."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content
