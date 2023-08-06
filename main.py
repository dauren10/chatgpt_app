import openai
KEY='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'


openai.api_key = KEY



def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine='gpt-3.5-turbo-0613',#model
        max_tokens=10,
        temperature=0.7,#креативность
        n=1,#варианты
        stop=None,
        timeout=15
    )
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None
    
res = generate_response("Привет, какая погода в Алматы?")
print(res)