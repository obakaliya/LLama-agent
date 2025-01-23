from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.utils.pprint import pprint_run_response

load_dotenv()

# Initialize memory (to store past user inputs and agent responses)
memory = []

# Create agent
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources", 'user preview data to gain understanding and answer queries better'],
    show_tool_calls=True,
    markdown=True,
)

def update_memory(user_input, agent_response):
    memory.append({'user_input': user_input, 'agent_response': agent_response})
    if len(memory) > 10:  # Limit memory size
        memory.pop(0)  # Remove oldest memory entry if needed

def get_past_context():
    # Build the context from memory (you could format this differently if needed)
    context = ""
    for entry in memory:
        context += f"User: {entry['user_input']}\nAgent: {entry['agent_response']}\n\n"
    return context

while True:
    print("Enter your text: ")
    user_input = input()
    
    # Get previous context and append current input to it
    context = get_past_context()
    
    # Combine past context with the new input
    full_input = context + f"User: {user_input}\nAgent:"
    
    # Get response from the agent
    agent_response = web_agent.run(full_input)
    pprint_run_response(agent_response, markdown=True, show_time=True)

    # Print and store the response in memory
    # print(agent_response)
    update_memory(user_input, agent_response)
