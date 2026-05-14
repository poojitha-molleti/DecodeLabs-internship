def chatbot():
    print(" ChatBot: Hello! I am your simple AI chatbot.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print(" ChatBot: Goodbye! Have a great day ")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print(" ChatBot: Hello! How can I help you?")
        elif "your name" in user_input:
            print(" ChatBot: I am a rule-based chatbot created by you!")

        elif "ai" in user_input:
            print(" ChatBot: AI stands for Artificial Intelligence. It helps machines think like humans.")

        elif "study" in user_input or "exam" in user_input:
            print(" ChatBot: Stay consistent. Even 1 hour daily matters!")

        elif "weather" in user_input:
            print(" ChatBot: I can't check real weather, but I hope it's a great day!")

        elif "help" in user_input:
            print(" ChatBot: You can ask me about AI, studies, or general questions!")

        else:
            print(" ChatBot: Sorry, I don't understand that yet. Try something else.")

chatbot()