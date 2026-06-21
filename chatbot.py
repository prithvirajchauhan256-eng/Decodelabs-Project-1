import datetime

print("=" * 50)
print("🤖 Welcome to DecodeBot")
print("Created by Prithvi Raj")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")


    elif user_input == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user_input == "who created you":
        print("Bot: I was created by Prithvi Raj during his AI internship.")

    elif user_input == "how are you":
        print("Bot: I am doing great. Thanks for asking!")


    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user_input == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)


    elif user_input == "favorite color":
        print("Bot: My favorite color is blue.")


    elif user_input == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs! 😂")


    elif user_input == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Sum =", num1 + num2)

    elif user_input == "subtract":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Difference =", num1 - num2)

    elif user_input == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Product =", num1 * num2)

    elif user_input == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 != 0:
            print("Bot: Quotient =", num1 / num2)
        else:
            print("Bot: Cannot divide by zero.")


    elif user_input == "help":
        print("\nAvailable Commands:")
        print("hello / hi / hey")
        print("how are you")
        print("what is your name")
        print("who created you")
        print("date")
        print("time")
        print("favorite color")
        print("tell me a joke")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("bye")


    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day. 👋")
        break


    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")