import requests

while True:
    userInput = input("Enter some starter text here for the model to generate the rest of the story\n")


    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': userInput,
        },
        headers={'api-key': '8f07d761-eebb-47f1-86ff-dadec25d71ca'}
    )
    print("\n\n\n\n")
    print(r.json()['output'])
    print("\n\n\n\n")