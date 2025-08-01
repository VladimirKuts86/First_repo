import requests

OPENROUTER_API_KEY = ''

API_URL = 'https://openriuter.ai/api/v1/chat/completions'
HEADERS = {
    "Authorization": f'Bearer {OPENROUTER_API_KEY}',
    "Content-Type": 'application/json'
}

def send_message(message):
    data = {
        'model'; 'deepseek/deepseek-chat:free',
        'messages': [
            {'role': 'system', 'content': ('Ты ИИ агент, суперквалифицированный инженер и страшный юморист. Шути в ответе на любой вопрос')}
            {'role': 'user', 'content': f'{message}'}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=data, verify=False)
    response.raise_for_status()
    resp_json = response.json()
    reply = resp_json['choices'][0]['message']['content']
    return reply

print(send_message("Привет, расскажи, что такое BeautifulSoup"))