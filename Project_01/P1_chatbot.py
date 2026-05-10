def start_chatbot():
    responses = {
        "hello": "Hi there! I am Kynova, your assistant. How can I help you today?",
        "hi": "Hello! Kynova here. Ready to build some AI systems?",
        "who are you": "I am Kynova, a rule-based AI chatbot built for Project 1.",
        "project 1": "Project 1 is the foundation phase: The Rule-Based AI Chatbot.",
        "decodelabs": "DecodeLabs is where you master the art of teaching machines.",
        "help": "You can greet me, ask about my identity, or type 'exit' to quit."
    }

    print("--- Kynova AI Initialized ---")
    print("(Type 'exit' to close the program)")

    
    while True:
       
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

       
        if clean_input == 'exit':
            print("Kynova: Goodbye! Transitioning from logic to learning.")
            break 

       
        reply = responses.get(clean_input, "I do not understand. Please try another command.")
        
       
        print(f"Kynova: {reply}")

if __name__ == "__main__":
    start_chatbot()