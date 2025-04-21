import nltk
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# List of possible greetings

greetings = ['hello', 'hi', 'hey', 'greetings']

# Dictionary of responses
responses = {
    'hello': 'Hello! How can I assist you?',
    'how are you': 'I\'m doing well, thanks!',
    'what is your name': 'My name is ChatBot',
}

# Function to process user input
def process_input(user_input):
    user_input = user_input.lower()
    user_input = lemmatizer.lemmatize(user_input)

    # Check if it's a greeting
    for greeting in greetings:
        if greeting in user_input:
            return responses['hello']

    # Check if input matches a known phrase
    for response in responses:
        if response in user_input:
            return responses[response]

    # Default fallback response
    return 'I didn\'t understand that.'

# Main chatbot function
def chatbot():
    print('Welcome to the chatbot!')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        print('ChatBot:', process_input(user_input))

# Run the chatbot
chatbot()