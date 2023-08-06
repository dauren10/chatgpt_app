import requests
gpt_key ='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'


def generate(message):
    url= 'https://api.openai.com/v1/images/generations'

    headers = {
        'Authorization':f'Bearer {gpt_key}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json={"prompt":message}, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print('Error', response.text)


text = 'Bugatti and Volvo'

generate(text)