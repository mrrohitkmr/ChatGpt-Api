import requests
import random

questions = [line.strip() for line in open("faq.txt", "r")]
random_question = random.choice(questions)

url = "http://127.0.0.1:8000/chatbot/"
data = {"question":random_question}
response = requests.post(url, json=data)
if response.status_code == 200:
    data = response.json()
    print(data)
    # do something with the JSON data
else:
    print("Error:", response.status_code)
