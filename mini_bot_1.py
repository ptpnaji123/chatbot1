def chatbot():
    print("Hello! I'm your chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hi! How are you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")

        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif "name" in user_input:
            print("Chatbot: I'm a chatbot. I don't have a name, but you can call me whatever you like!")

        elif "favorite" in user_input:
            print("Chatbot: I don't have favorites, but I love helping people like you!")

        elif "help" in user_input:
            print("Chatbot: Sure! Ask me anything and I'll try to help.")

        elif "age" in user_input:
            print("Chatbot: I don't age. I'm always here to chat with you!")

        elif "joke" in user_input:
            print("Chatbot: Why don’t skeletons fight each other? They don’t have the guts!")

        elif "weather" in user_input:
            print("Chatbot: I can't check the weather, but you can easily find it on your phone!")

        else:
            print("Chatbot: I didn't understand that. Can you try asking something else?")


chatbot()
