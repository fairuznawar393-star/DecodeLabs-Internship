print("Chatbot: Hello! Type 'bye', 'exit', or 'quit' to end the chat.")
responses={"hello": "Hello! How can I help you today?", 
           "hi": "Hi! How can I help you today?",
           "hey":"Hey! How can I help you today?",
           "how are you":"I'm doing well. Thanks for asking!",
           "what is your name":"I'm a simple rule-based chatbot.",
           "bye":"Goodbye! Have a great day!",
           "exit":"Exiting the chatbot. Goodbye!",
           "quit":"Goodbye! It was nice chatting with you."
           }
while True:
  user_input = input("You: ").lower().strip()
  print("Chatbot:", responses.get(user_input, "Sorry, I do not understand."))

  if user_input in ["bye", "exit", "quit"]:
    break