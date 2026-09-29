
import ollama
print("type exit to stop \n")
while True:
    q = input("YOU:")
    if q.lower() == "exit":
        print("AI:good bye")
        break
    response = ollama.chat(
        model = "llama3.2",messages=[{
            "role": "user",
            "content": q
        }]
    )
    print("BOT:",response["message"]["content"])