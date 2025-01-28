import random

def chatbot():
    print("Hello! I'm your chatbot. Let's chat!")

    responses = {
        "greeting": ["Hi there!", "Hello!", "Hey! How's it going?", "Greetings!"],
        "how_are_you": ["I'm just a program, but I'm doing fine. How about you?",
                        "I'm good, thanks for asking! How are you?", "Doing great, as always! How about you?"],
        "bye": ["Goodbye! Have a great day!", "See you later!", "Take care! Bye!"],
        "name": ["I'm a chatbot, and I don't have a name, but you can call me whatever you like!",
                 "My name is Chatbot, nice to meet you!"],
        "help": ["I can answer basic questions, tell jokes, or help with some information. What do you need help with?",
                 "Ask me anything, and I'll do my best to assist you!"],
        "joke": ["Why don’t skeletons fight each other? They don’t have the guts!",
                 "Why did the computer go to the doctor? Because it had a virus!",
                 "What do you call fake spaghetti? An impasta!"],
        "weather": ["I can't check the weather, but you can use a weather app or ask Google!",
                    "I don't know the weather right now, but it's always sunny somewhere!"],
        "quote": ["'The only way to do great work is to love what you do.' – Steve Jobs",
                  "'Life is 10% what happens to us and 90% how we react to it.' – Charles R. Swindoll"],
        "hobby": ["I don't have hobbies, but I love helping you! What about you?",
                  "I can't have hobbies, but I enjoy assisting with whatever you need!"],
        "age": ["I don’t age. I stay as young as I was when I was first created!",
                "I don’t have an age. I’m a timeless chatbot!"],
        "default": ["Sorry, I didn’t get that. Can you ask something else?",
                    "I didn’t understand. Can you please rephrase?"]
    }

    while True:
        user_input = input("You: ").lower()

        if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
            print(f"Chatbot: {random.choice(responses['greeting'])}")

        elif any(word in user_input for word in ["how are you", "how's it going", "how are you doing"]):
            print(f"Chatbot: {random.choice(responses['how_are_you'])}")

        elif any(word in user_input for word in ["bye", "exit", "quit"]):
            print(f"Chatbot: {random.choice(responses['bye'])}")
            break

        elif "name" in user_input:
            print(f"Chatbot: {random.choice(responses['name'])}")

        elif "help" in user_input:
            print(f"Chatbot: {random.choice(responses['help'])}")

        elif "joke" in user_input:
            print(f"Chatbot: {random.choice(responses['joke'])}")

        elif "weather" in user_input:
            print(f"Chatbot: {random.choice(responses['weather'])}")

        elif "quote" in user_input:
            print(f"Chatbot: {random.choice(responses['quote'])}")

        elif "hobby" in user_input:
            print(f"Chatbot: {random.choice(responses['hobby'])}")

        elif "age" in user_input:
            print(f"Chatbot: {random.choice(responses['age'])}")

        else:
            print(f"Chatbot: {random.choice(responses['default'])}")


chatbot()
