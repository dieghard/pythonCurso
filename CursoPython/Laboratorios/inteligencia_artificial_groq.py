#Recuerda usar pip install groq
from groq import Groq

client = Groq(
    api_key="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",
)
while True:
    print("Hola, a continuacion podras preguntarle lo que quieras a la inteligencia artificial")

    while True:
        prompt = input("Ingrese lo que quieras preguntarle a la Inteligencia Artificial, si deseas salir puedes colocar la letra Q(quit): ").capitalize()
        if prompt == "Q":
            break
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        print(chat_completion.choices[0].message.content)
    flag = input("Si quieres dejar de usar la inteligencia artificial coloca SALIR, en caso contrario coloca cualquier cosa y volverás a comenzar:").upper()
    if flag == "SALIR":
        exit()