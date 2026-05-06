# Assignment 5
# Name: Krushna Keshav Garole
# Roll No: C32257


def chatbot():

    print("Welcome to Customer Support Chatbot!")
    print("Type 'exit' to end chat.\n")

    while True:

        user = input("You: ").lower()

        # Exit condition
        if user == "exit":
            print("Bot: Thank you! Have a great day.")
            break

        # Greeting
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I assist you today?")

        # Price query
        elif "price" in user:
            print("Bot: Our products range from ₹500 to ₹5000.")

        # Product query
        elif "product" in user:
            print("Bot: We offer electronics, clothing, and accessories.")

        # Order query
        elif "order" in user:
            print("Bot: You can place an order on our website.")

        # Delivery query
        elif "delivery" in user:
            print("Bot: Delivery takes 3-5 business days.")

        # Return query
        elif "return" in user:
            print("Bot: You can return products within 7 days.")

        # Unknown query
        else:
            print("Bot: Sorry, I didn't understand. Can you rephrase?")


# Run chatbot
chatbot()