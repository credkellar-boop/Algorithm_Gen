import os
from dotenv import load_dotenv
from generator.main import process_prompt

def main():
    # Load secret API keys from the .env file
    load_dotenv()
    
    print("Welcome to the AI Algorithm Generator!")
    print("Type 'exit' or 'quit' to stop.")
    
    while True:
        user_input = input("\nEnter your algorithm request: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down. Goodbye!")
            break
        
        result = process_prompt(user_input)
        print("\n--- Generated Algorithm ---")
        print(result)

if __name__ == "__main__":
    main()
  
