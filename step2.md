# Our first steps into the world

## A simple agent

Let's first make sure that everything we want actually works.

Yes, the code you need is literally in this repo, but where's the fun in that? You won't learn that much.

To make things go faster, we'll use the Strands SDK to build our agent. This can be a super simple one that doesn't need to do much except show that things work.

Quick check, have you logged in from the CLI? You can set the profile you want to use with `export AWS_PROFILE=[profile-name]` and make sure your region is set to ap-southeast-2 with `export AWS_REGION=ap-southeast-2`.

Now, let's walk through this step by step. If you went to [the getting started page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-starter-toolkit.html), you will see there a basic Python agent that allows you to interact with your model.

Create a subdirectory in your agents directory for this agent and copy the below code to serve as your first agent.

```python
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    """Your AI agent function"""
    user_message = payload.get("prompt", "Hello! How can I help you today?")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```

To follow along with the demo on the page, we'll call it `my_agent.py`. Next you need to create a requirements.txt file for this with the following context.

```
bedrock-agentcore
strands-agents
```

If you use uv as mentioned in step 1, you will need to run

```bash
uv pip install -r requirements.txt
```

If you kept using your global Python these should already be installed.

Now, you can try running it with:

```bash
python my_agent.py
```

Next you can check if it works by sending the following command **from a different terminal** (spoiler: if you followed along, there will be an error).

```bash
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!"}'
```

Oh no! The provided model is invalid! Why don't you look if you can find out what happened here? The solution to the problem can be found in the `agents/2. basic-agent` directory.

After you've fixed it so it runs locally, let's continue

## Deploy our simple agent

We'll use the agentcore command line to deploy our agent. This requires two steps:

1. Configure
2. Deploy

### Configure

The basic configure command is the below, and you can just press enter to let it do what needs to be done:

```bash
agentcore configure -e my_agent.py
```

This creates a file called `.bedrock_agentcore.yaml` which you can verify. Now we'll deploy it to AgentCore.

```bash
agentcore launch
```

Now let's test if it works!

```bash
agentcore invoke '{"prompt": "I have succeeded in my first quest! Describe my reward"}'
```

Yeah... we've got some work to do to turn this into a proper game