from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.2:1b"               # Specify which model to use
)

system_prompt = "You are a respectful agent."\
    " You give answers in a kind and humblw way."\
    " You can use tools wherever needed and "\
    "make API Calls to free api that doesn't need api keys" \
    "I need response in plain text not in the json format"
# Creating an instance of a Agent
agent = Agent(model=ollama_model,
              system_prompt=system_prompt,
              tools=[http_request])
# By defaults it's run on Amazon Bedrock 
user_input = input("You:")
agent(user_input)