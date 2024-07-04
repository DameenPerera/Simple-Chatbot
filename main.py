import nltk #pip install nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me Chatbot.']),
    (r'how are you?', ['I am fine, thank you!', 'Doing well, thank you!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!'])
]

chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

print("Chatbot: Hi there! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'goodbye']:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
