import ollama

def call_ollama(input):
    content = input
    response = ollama.chat(model='dolphin-llama3', messages=[
    {
        'role': 'user',
        'content': input,
    },
    ])
    print(response['message']['content'])
    answer = response['message']['content']
    return answer

