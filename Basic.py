import openai
import requests
import webbrowser
from PIL import Image
from io import BytesIO

openai.api_key = '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'

query = input("질문을 입력하세요: ")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query},
        {"role": "user", "content": "단답"},
        {"role": "user", "content": "입니다 빼고"}
    ]
)

answer = response['choices'][0]['message']['content']
print(answer)

response2 = openai.Image.create(
  prompt=answer,
  n=1,
  size="1024x1024"
)

image_url = response2['data'][0]['url']
webbrowser.open_new(image_url)
