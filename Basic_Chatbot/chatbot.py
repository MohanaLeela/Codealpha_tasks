# Basic Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I'm Python Chatbot!"

    elif user_input == "i am fine":
        return "That's great to hear!"

    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Try something else."


# Main program
print("===================================")
print("       WELCOME TO CHATBOT")
print("===================================")

print("Type 'bye' to exit the chatbot.\n")

# Continuous conversation
while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    # Exit condition
    if user_input.lower() == "bye":
        break

print("\nChatbot session ended!")