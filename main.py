print("===== Basic Chatbot =====")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi! Welcome.")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: My name is Python Chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand.")
        