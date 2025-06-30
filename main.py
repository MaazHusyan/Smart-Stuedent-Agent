from agents.openrouter_agent import ask_llm_via_openrouter

def main():
    print("🤖 Smart Student Agent is online. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("\n👨 You: ").strip()
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Bye! Stay smart.")
            break
        
        response = ask_llm_via_openrouter(user_input)
        print("\n🤖 Agent:", response)

if __name__ == "__main__":
    main()
