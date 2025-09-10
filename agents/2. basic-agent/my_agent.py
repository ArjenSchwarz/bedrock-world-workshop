from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent(model="amazon.nova-lite-v1:0")

@app.entrypoint
def invoke(payload):
    """Your AI agent function"""
    user_message = payload.get("prompt", "Hello! Welcome to the world of Bedrock! A world full of adventure.")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
