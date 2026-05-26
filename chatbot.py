import random
import datetime



name = input("Enter your name : ")

print("      WELCOME TO SMART CHATBOT")


print("Hello", name + "!")
print("Type 'bye' anytime to exit.\n")


# Random greeting messages
greetings = [
    "Hello 😊",
    "Hi there 😄",
    "Hey friend 👋",
    "Nice to meet you 😊"
]

# Question counter
count = 0


# Chatbot loop
while True:

    # Taking user input
    message = input("You : ").lower()

    # Counting questions
    count += 1

    # Greeting messages
    if message in ["hi", "hello", "hey"]:
        print("Bot :", random.choice(greetings))

    # Asking chatbot name
    elif "your name" in message:
        print("Bot : My name is Smart ChatBot.")
    
    elif "deep meaning of life" in message:
        print("Formal Education will make you a living. Experiences will teach you how to live")

    # Asking creator
    elif "who created you" in message:
        print("Bot : I was created using Python programming.")

    # Asking health
    elif "how are you" in message:
        print("Bot : I am doing great. Thank you!")

    # Asking about Python
    elif "what is python?" in message:
        print("Bot : Python is a simple and powerful programming language.")

    # Asking about college
    elif "tell me about college life and memories" in message:
        print("Bot : College life is very interesting and fun. We learn a lot from our faculty, friends. Sometimes the best lesson's come from friends and rral-life experiences, not from textbooks.")

    # Asking about AI
    elif "artificial intelligence" in message or "ai" in message:
        print("Bot : AI means machines behaving like humans.")

    # Showing current time
    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot : Current time is", current_time)

    # Showing current date
    elif "date" in message:
        today = datetime.date.today()
        print("Bot : Today's date is", today)

    # Thank you message
    elif "thank you" in message or "thanks" in message:
        print("Bot : You are welcome 😊")

    # Help section
    elif "help" in message:
        print("Bot : You can ask me about:")
        print("- Python")
        print("- AI")
        print("- Time")
        print("- Date")
        print("- Jokes")
        print("- Motivation")

    # Joke section
    elif "hey bot tell me a joke" in message:
        print("Bot : Why do programmers hate nature? Because it has too many bugs 😂")

    # Motivation section
    elif "can you please motivate me" in message:
        print("Bot : Believe in yourself. Success will come one day 💪")

    # Favorite color
    elif "what is your favorite color?" in message:
        print("Bot : My favorite color is blue 💙")

    # Marks section
    elif "how to score good marks" in message:
        print("Bot : Study consistently and you will get excellent marks.")

    # Simple math
    elif "2 + 2" in message:
        print("Bot : The answer is 4")

    elif "5 + 5" in message:
        print("Bot : The answer is 10")

    # Asking bot age
    elif "your age" in message:
        print("Bot : I am a newly created chatbot 😄")

    # Asking user name
    elif "my name" in message:
        print("Bot : Your name is", name)

    # Exit condition
    elif message in ["bye", "exit", "quit"]:
        print("\nBot : Goodbye", name + "!")
        print("Bot : Have a wonderful day 😊")
        print("Bot : Total questions asked =", count)
        break

    # Default response
    else:
        print("Bot : Sorry, I don't understand your question.")