import os

from groq import Groq

api_key = "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"

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)