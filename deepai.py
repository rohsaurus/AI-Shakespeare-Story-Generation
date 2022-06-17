import requests

userInput = input("Enter some starter text here for the model to generate the rest of the story\n")


r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': userInput,
    },
    headers={'api-key': 'fc29a633-b891-4204-8db0-ac87cd81226b'}
)
print("\n\n\n\n")
print(r.json()['output'])