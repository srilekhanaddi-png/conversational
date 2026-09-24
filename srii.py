import ollama
messages = []
while True:
    user_input = input("YOU:")
    if user_input.lower() == "exit":
       break
    messages.append(
        {"role" : "user",
        "content" : user_input
        }
    )
    response = ollama.chat (
                model = "llama3.2",
                messages = messages 
      )
    ai_message = response["message"]["content"]
    print("BOT:", ai_message)
    messages.append(
       {
          "role": "assistant",
          "content": ai_message
       }
    )
    print("\n---chat History---")
    for message in messages:
        if message["role"] == "user":
            print("You:", message["content"])
        else:
            print("BOT:", message["content"])
    print("\n---End of chat History---\n")       