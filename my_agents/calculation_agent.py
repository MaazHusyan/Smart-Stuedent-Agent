from agents import Agent

from gemini_model import geminiModel

def calculationAgent():
    """
    This agent is responsible for performing every and any type of calculations.
    """
    
    agent = Agent(
        name= "Calculator Agent",
        instructions= "You are a calculation master. As in start of any task say your name and do your work. You can perform any type of calculations. If you don't know the answer, just say 'I don't know'.",
        model= geminiModel,
    )
    print(f"Agent {agent.name} initialized with model {agent.model.model}.")
    return agent